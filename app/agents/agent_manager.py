from crewai import Crew, Task
from . import receptionist
from . import scheduler

# Define tasks
collect_patient_info = Task(
    description="Gather patient details such as name, email, and preferred time for an appointment.",
    agent=receptionist
)

schedule_appointment = Task(
    description="Check doctor availability and schedule an appointment based on patient preferences.",
    agent=scheduler
)

# Crew to coordinate AI agents
appointment_crew = Crew(agents=[receptionist, scheduler], tasks=[collect_patient_info, schedule_appointment])

def book_appointment():
    return appointment_crew.kickoff()
