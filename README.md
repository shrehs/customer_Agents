# customer_Agents
# AI-Powered Medical Appointment Scheduling

## Overview

This project is an AI-driven **customer support system** for medical appointment scheduling. It uses **FastAPI**, **CrewAI**, and **OpenAI API** to automate booking appointments, checking doctor availability, and handling patient queries efficiently.

## Features

- **AI-Powered Receptionist & Scheduler**: Uses **CrewAI** to handle user queries and schedule appointments.
- **JWT Authentication**: Secure login system for patients.
- **Database Integration**: Uses **SQLAlchemy** to store appointment and doctor details.
- **FastAPI Endpoints**: RESTful API for appointment booking and user authentication.
- **Cloud Deployment**: Ready for deployment using **Render/Railway/AWS**.

---

## Tech Stack

- **Backend**: FastAPI, Python
- **Database**: PostgreSQL (SQLite for local development)
- **AI**: OpenAI GPT-4 for natural language responses
- **Authentication**: JWT Authentication (fastapi\_jwt\_auth)
- **Task Management**: CrewAI for coordinating AI agents
- **Deployment**: Render / Railway / AWS

---

## Installation Guide

### 1. Clone the Repository

```sh
git clone https://github.com/your-repo/medical-appointment-ai.git
cd medical-appointment-ai
```

### 2. Set Up Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a **.env** file and add the following:

```sh
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./database.db  # Change for PostgreSQL in production
JWT_SECRET=your_secret_key_here
```

### 5. Fix Import Errors (if any)

If you encounter **ImportError: No module named 'fastapi\_jwt\_auth'**, install it manually:

```sh
pip install fastapi-jwt-auth
```

---

## Running the Application

```sh
uvicorn main:app --reload
```

The API will run at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

## API Endpoints

### 1. **User Authentication**

- **Login**: `POST /auth/login`
- **Register**: `POST /auth/register`

### 2. **Appointments**

- **Book an appointment**: `POST /appointments/book`
- **Check doctor availability**: `GET /doctors/{doctor_id}`

---

## AI Agents

This project uses **CrewAI** to automate patient interactions:

1. **Receptionist Agent**: Collects patient details and responds to queries.
2. **Scheduler Agent**: Checks doctor availability and books appointments.

```python
from agents.receptionist import receptionist
from agents.scheduler import scheduler
from crewai import Crew, Task

collect_patient_info = Task(description="Gather patient details.", agent=receptionist)
schedule_appointment = Task(description="Schedule an appointment.", agent=scheduler)

appointment_crew = Crew(agents=[receptionist, scheduler], tasks=[collect_patient_info, schedule_appointment])
```

---

## Testing the API

### **1. Using Swagger UI**

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

### **2. Using cURL**

#### **Login**

```sh
curl -X 'POST' 'http://127.0.0.1:8000/auth/login' -H 'Content-Type: application/json' \
-d '{"email": "alice@example.com", "password": "secure123"}'
```

#### **Book an Appointment**

```sh
curl -X 'POST' 'http://127.0.0.1:8000/appointments/book' -H 'Content-Type: application/json' \
-d '{"patient_id": 1, "doctor_id": 2, "appointment_time": "2025-02-06 10:30:00"}'
```

---

## Last Two Steps to Complete

1. **AI Enhancements**

   - Improve **CrewAI** logic for natural conversation.
   - Add the model and train.
   - Enhance **GPT-4** responses in `receptionist.py`.

2. **Deployment**

   - Deploy **FastAPI app** using **Render, Railway, or AWS**.
   - Setup **PostgreSQL** for production.

---

## Contributors

Feel free to fork, contribute, or open issues! 🚀


