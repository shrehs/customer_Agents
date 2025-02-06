from fastapi import FastAPI
from routes import auth, appointments, doctors

app = FastAPI()

# Include the routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])

@app.get("/")
def home():
    return {"message": "Welcome to the AI Medical Appointment System"}
