#!/bin/bash

# Quick start script for remote development teams
# This script sets up the Customer Agents project for immediate remote work

set -e

echo "🌐 Customer Agents - Remote Development Quick Start"
echo "=================================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "🔍 Checking prerequisites..."

if ! command_exists git; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

if ! command_exists docker; then
    echo "⚠️ Docker is not installed. You can install dependencies manually or install Docker for containerized development."
    DOCKER_AVAILABLE=false
else
    echo "✅ Docker is available"
    DOCKER_AVAILABLE=true
fi

if ! command_exists python3; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Prerequisites check complete"
echo ""

# Offer development options
echo "🚀 Choose your development setup:"
echo "1. Docker Setup (Recommended for teams) - Isolated, consistent environment"
echo "2. Local Python Setup - Direct installation on your machine"
echo "3. Show project structure only"
echo ""

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "🐳 Setting up Docker development environment..."
        
        if [ "$DOCKER_AVAILABLE" = false ]; then
            echo "❌ Docker is not available. Please install Docker and Docker Compose first."
            echo "Visit: https://docs.docker.com/get-docker/"
            exit 1
        fi
        
        # Create .env from template
        if [ ! -f ".env" ]; then
            cp .env.example .env
            echo "✅ Created .env file from template"
            echo "⚠️ Edit .env file to add your OpenAI API key before running the application"
        fi
        
        echo "🏗️ Building and starting Docker containers..."
        docker-compose up --build -d
        
        echo "✅ Docker setup complete!"
        echo ""
        echo "🌐 Access your application:"
        echo "   API: http://localhost:8000"
        echo "   Docs: http://localhost:8000/docs"
        echo "   Database: PostgreSQL on localhost:5432"
        echo ""
        echo "📋 Useful commands:"
        echo "   View logs: docker-compose logs -f"
        echo "   Stop services: docker-compose down"
        echo "   Restart: docker-compose restart"
        echo "   Shell access: docker-compose exec web bash"
        ;;
        
    2)
        echo ""
        echo "🐍 Setting up local Python development environment..."
        
        # Run the main setup script
        ./setup.sh
        
        echo "✅ Local setup complete!"
        echo ""
        echo "🚀 To start development:"
        echo "   1. source venv/bin/activate"
        echo "   2. uvicorn app.main:app --reload"
        echo "   3. Open http://localhost:8000/docs"
        ;;
        
    3)
        echo ""
        echo "📁 Customer Agents Project Structure:"
        echo "================================="
        tree -I '__pycache__|*.pyc|venv|.git|node_modules' -L 3 2>/dev/null || find . -type f -name "*.py" -o -name "*.yml" -o -name "*.md" -o -name "Dockerfile" | head -20
        echo ""
        echo "📖 Key files for remote development:"
        echo "   📄 README.md - Complete setup guide"
        echo "   🐳 Dockerfile - Container configuration"
        echo "   🔧 docker-compose.yml - Development services"
        echo "   ⚙️ .env.example - Environment template"
        echo "   📦 requirements.txt - Python dependencies"
        echo "   🧪 .github/workflows/ - CI/CD automation"
        echo ""
        echo "🚀 Quick start: ./quick-start.sh"
        ;;
        
    *)
        echo "❌ Invalid choice. Please run the script again and choose 1, 2, or 3."
        exit 1
        ;;
esac

echo ""
echo "📚 Additional Resources:"
echo "   📖 Full documentation: README.md"
echo "   🐛 Troubleshooting: See README.md#troubleshooting"
echo "   🔧 CI/CD pipeline: .github/workflows/ci-cd.yml"
echo ""
echo "🎉 Happy coding! The Customer Agents project is ready for remote development."