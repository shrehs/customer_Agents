from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import SessionLocal
from database.models import Patient
import bcrypt
from fastapi_jwt_auth import AuthJWT #Issue in importing the lib

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(name: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    new_patient = Patient(name=name, email=email, password=hashed_password)
    db.add(new_patient)
    db.commit()
    return {"message": "User registered successfully"}
