from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from sqlalchemy import func
from datetime import date
router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Total items sold (dummy logic for now)
@router.get("/items-sold")
def get_items_sold(db: Session = Depends(get_db)):
    total = db.query(func.sum(models.Sale.quantity_sold)).scalar() or 0
    return {"items_sold": total}


# ✅ Low stock items
@router.get("/low-stock")
def low_stock(db: Session = Depends(get_db)):
    items = db.query(models.Medicine).filter(models.Medicine.quantity < 10).all()
    return items


# ✅ Sales summary
@router.get("/sales-summary")
def sales_summary(db: Session = Depends(get_db)):
    today = date.today()

    total_sales = db.query(func.sum(models.Sale.total_price))\
        .filter(models.Sale.date == today)\
        .scalar() or 0

    return {"today_sales": total_sales}

# ✅ Purchase summary
@router.get("/purchase-summary")
def purchase_summary(db: Session = Depends(get_db)):
    total_purchase = db.query(func.sum(models.Purchase.total_cost)).scalar() or 0
    return {"total_purchase_value": total_purchase}
@router.get("/recent-sales")
def recent_sales(db: Session = Depends(get_db)):
    sales = db.query(models.Sale)\
        .order_by(models.Sale.date.desc())\
        .limit(5)\
        .all()

    return sales
