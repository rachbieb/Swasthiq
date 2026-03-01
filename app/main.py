from fastapi import FastAPI
from app.database import Base, engine
from app.routers import inventory, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pharmacy Backend")

app.include_router(inventory.router)
app.include_router(dashboard.router)
@app.get("/")
def root():
    return {"message": "Pharmacy API running 🚀"}
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend.vercel.app",
        "https://your-frontend.netlify.app",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)