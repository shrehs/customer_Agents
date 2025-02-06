from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Example endpoint for scheduling an appointment
@router.post("/schedule")
def schedule_appointment(patient_id: int, doctor_id: int, appointment_time: str):
    return {"message": f"Appointment scheduled for patient {patient_id} with doctor {doctor_id} at {appointment_time}"}
