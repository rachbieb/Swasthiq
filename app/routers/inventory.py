from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.utils.status import get_medicine_status
router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Get all medicines
@router.get("/")
def list_medicines(db: Session = Depends(get_db)):
    return db.query(models.Medicine).all()


# ✅ Add medicine
@router.post("/")
def add_medicine(medicine: schemas.MedicineCreate, db: Session = Depends(get_db)):
    status = get_medicine_status(medicine.expiry_date, medicine.quantity)

    new_med = models.Medicine(**medicine.dict(), status=status)

    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return new_med


# ✅ Update medicine
@router.put("/{med_id}")
def update_medicine(med_id: int, data: schemas.MedicineCreate, db: Session = Depends(get_db)):
    med = db.query(models.Medicine).filter(models.Medicine.id == med_id).first()

    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")

    for key, value in data.dict().items():
        setattr(med, key, value)

    med.status = get_medicine_status(data.expiry_date, data.quantity)

    db.commit()
    return med


# ✅ Mark status
@router.patch("/{med_id}/status")
def update_status(med_id: int, status: str, db: Session = Depends(get_db)):
    med = db.query(models.Medicine).filter(models.Medicine.id == med_id).first()

    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")

    med.status = status
    db.commit()
    return med
@router.get("/search")
def search_medicines(
    name: str = None,
    category: str = None,
    status: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Medicine)

    if name:
        query = query.filter(models.Medicine.name.ilike(f"%{name}%"))

    if category:
        query = query.filter(models.Medicine.category == category)

    if status:
        query = query.filter(models.Medicine.status == status)

    return query.all()