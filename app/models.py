from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    batch_no = Column(String)
    expiry_date = Column(Date)
    quantity = Column(Integer)
    price = Column(Float)
    status = Column(String)  # Active, Low Stock, Expired, Out of Stock
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from .database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    quantity_sold = Column(Integer)
    total_price = Column(Float)
    date = Column(Date)


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    quantity_bought = Column(Integer)
    total_cost = Column(Float)
    date = Column(Date)