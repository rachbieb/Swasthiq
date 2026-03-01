from app.database import SessionLocal, engine
from app import models
from datetime import date

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_data = [
    {
        "name": "Paracetamol",
        "category": "Tablet",
        "batch_no": "PCM123",
        "expiry_date": date(2026, 5, 10),
        "quantity": 50,
        "price": 10.5,
        "status": "Active"
    },
    {
        "name": "Crocin",
        "category": "Tablet",
        "batch_no": "CRC456",
        "expiry_date": date(2024, 1, 1),
        "quantity": 5,
        "price": 8.0,
        "status": "Low Stock"
    },
]

for item in sample_data:
    med = models.Medicine(**item)
    db.add(med)

db.commit()
db.close()
from app.database import SessionLocal, engine
from app import models
from datetime import date
import random

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Get medicines
medicines = db.query(models.Medicine).all()

# Create Sales
for _ in range(20):
    med = random.choice(medicines)
    qty = random.randint(1, 5)

    sale = models.Sale(
        medicine_id=med.id,
        quantity_sold=qty,
        total_price=qty * med.price,
        date=date.today()
    )
    db.add(sale)

# Create Purchases
for _ in range(10):
    med = random.choice(medicines)
    qty = random.randint(10, 50)

    purchase = models.Purchase(
        medicine_id=med.id,
        quantity_bought=qty,
        total_cost=qty * med.price,
        date=date.today()
    )
    db.add(purchase)

db.commit()
db.close()