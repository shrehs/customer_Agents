import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database.config import Base
from database.models import Patient, Doctor


# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db_session():
    """Create a fresh database session for each test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    """Create a test client."""
    with TestClient(app) as c:
        yield c


@pytest.fixture
def sample_patient(db_session):
    """Create a sample patient for testing."""
    patient = Patient(
        name="John Doe",
        email="john@example.com",
        password="hashed_password",
        phone="1234567890"
    )
    db_session.add(patient)
    db_session.commit()
    db_session.refresh(patient)
    return patient


@pytest.fixture
def sample_doctor(db_session):
    """Create a sample doctor for testing."""
    doctor = Doctor(
        name="Dr. Smith",
        specialization="Cardiology",
        available_slots='["09:00", "10:00", "11:00"]'
    )
    db_session.add(doctor)
    db_session.commit()
    db_session.refresh(doctor)
    return doctor