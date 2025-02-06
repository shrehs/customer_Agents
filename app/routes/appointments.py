from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import SessionLocal
from database.models import Appointment, Doctor
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book")
def book_appointment(patient_id: int, doctor_id: int, appointment_time: str, db: Session = Depends(get_db)):
    # Convert string to datetime
    try:
        appointment_datetime = datetime.strptime(appointment_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format. Use YYYY-MM-DD HH:MM:SS")

    # Check if doctor is available
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    # Save appointment
    new_appointment = Appointment(
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_time=appointment_datetime,
        status="Scheduled"
    )
    db.add(new_appointment)
    db.commit()
    return {"message": "Appointment booked successfully"}
