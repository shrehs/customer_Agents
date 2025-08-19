from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database.config import SessionLocal
from database.models import Patient
import hashlib

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(Patient).filter(Patient.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Simple password check (in production, use proper hashing)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if user.password != password_hash:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Return simple token (in production, use proper JWT)
    access_token = f"token_for_{user.email}"
    return {"access_token": access_token, "message": "Login successful"}

@router.post("/register")
def register(name: str, email: str, password: str, phone: str, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(Patient).filter(Patient.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password (simple implementation)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Create new user
    new_user = Patient(
        name=name,
        email=email,
        password=password_hash,
        phone=phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User registered successfully", "user_id": new_user.id}
