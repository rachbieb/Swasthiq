from fastapi import FastAPI
from app.database import Base, engine
from app.routers import inventory, dashboard
from fastapi.middleware.cors import CORSMiddleware

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create app ONLY ONCE
app = FastAPI(title="Pharmacy Backend")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://swasthiqfrontend06.vercel.app/",
        "https://your-frontend.netlify.app",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(inventory.router)
app.include_router(dashboard.router)

# Root route
@app.get("/")
def root():
    return {"message": "Pharmacy API running 🚀"}