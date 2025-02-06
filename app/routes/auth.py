from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from database.config import SessionLocal
from database.models import Patient
import bcrypt

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(email: str, password: str, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    user = db.query(Patient).filter(Patient.email == email).first()
    if not user or not bcrypt.checkpw(password.encode(), user.password.encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = Authorize.create_access_token(subject=user.email)
    return {"access_token": access_token}
