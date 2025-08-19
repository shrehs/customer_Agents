from . import receptionist
from . import scheduler

# Placeholder Task class for basic functionality
class MockTask:
    def __init__(self, description, agent):
        self.description = description
        self.agent = agent

# Placeholder Crew class
class MockCrew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks
    
    def kickoff(self):
        return {"message": "Appointment crew is ready to assist (AI features require full setup)"}

# Define tasks
collect_patient_info = MockTask(
    description="Gather patient details such as name, email, and preferred time for an appointment.",
    agent=receptionist.receptionist
)

schedule_appointment = MockTask(
    description="Check doctor availability and schedule an appointment based on patient preferences.",
    agent=scheduler.scheduler
)

# Crew to coordinate AI agents
appointment_crew = MockCrew(agents=[receptionist.receptionist, scheduler.scheduler], tasks=[collect_patient_info, schedule_appointment])

def book_appointment():
    return appointment_crew.kickoff()
