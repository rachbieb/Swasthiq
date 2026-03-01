from pydantic import BaseModel
from datetime import date

class MedicineCreate(BaseModel):
    name: str
    category: str
    batch_no: str
    expiry_date: date
    quantity: int
    price: float

class MedicineResponse(MedicineCreate):
    id: int
    status: str

    class Config:
        from_attributes = True