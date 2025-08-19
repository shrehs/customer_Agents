#!/bin/bash

# Development setup script for Customer Agents project
set -e

echo "🚀 Setting up Customer Agents for development..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file from template..."
    cp .env.example .env
    echo "⚠️ Please edit .env file with your actual API keys and configuration!"
fi

# Create data directory
mkdir -p data

# Initialize database
echo "🗄️ Setting up database..."
cd app
python -c "
from database.config import engine, Base
from database.models import Patient, Doctor, Appointment
Base.metadata.create_all(bind=engine)
print('Database tables created successfully!')
"
cd ..

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your OpenAI API key and other configuration"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Run the development server: uvicorn app.main:app --reload"
echo "4. Open http://localhost:8000/docs to see the API documentation"
echo ""
echo "For Docker setup:"
echo "1. Ensure Docker and Docker Compose are installed"
echo "2. Run: docker-compose up --build"