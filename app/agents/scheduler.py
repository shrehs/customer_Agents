from crewai import Agent

scheduler = Agent(
    name="Scheduler AI",
    role="Appointment Scheduler",
    goal="Find available slots and confirm appointments.",
    backstory="Handles scheduling tasks, ensuring smooth booking without conflicts."
)