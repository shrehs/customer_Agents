# Development Guide for Remote Teams

This guide provides detailed instructions for setting up and working with the Customer Agents project in a remote development environment.

## Quick Start for New Team Members

### Option 1: One-Command Setup (Recommended)
```bash
git clone https://github.com/shrehs/customer_Agents.git
cd customer_Agents
./quick-start.sh
```

### Option 2: Manual Setup
See the main [README.md](README.md) for detailed setup instructions.

## Remote Development Environments

### 1. GitHub Codespaces (Cloud Development)
1. Go to the repository on GitHub
2. Click "Code" → "Codespaces" → "Create codespace"
3. Wait for the environment to load
4. Run `./quick-start.sh` in the terminal

### 2. VS Code Remote Development
1. Install the Remote Development extension pack in VS Code
2. Clone the repository locally
3. Open the folder in VS Code
4. VS Code will automatically suggest installing recommended extensions
5. Use Ctrl+Shift+P → "Python: Select Interpreter" → Choose `./venv/bin/python`

### 3. Docker Development (Cross-Platform)
```bash
# Clone and start
git clone https://github.com/shrehs/customer_Agents.git
cd customer_Agents
cp .env.example .env
docker-compose up --build
```

## Development Workflow

### Daily Development
1. **Pull latest changes**: `git pull origin main`
2. **Activate environment**: `source venv/bin/activate` (or Docker)
3. **Install new dependencies**: `pip install -r requirements.txt`
4. **Run tests**: `pytest app/tests/`
5. **Start development server**: `uvicorn app.main:app --reload`

### Code Quality Checks
```bash
# Format code
black app/
isort app/

# Lint code
flake8 app/ --max-line-length=88

# Run tests
pytest app/tests/ -v --cov=app

# Security scan
bandit -r app/
```

### Environment Variables
Copy `.env.example` to `.env` and configure:
- `OPENAI_API_KEY`: Get from OpenAI Platform
- `DATABASE_URL`: SQLite for dev, PostgreSQL for production
- `JWT_SECRET`: Generate a secure 32+ character string

## CI/CD Pipeline

The project includes automated workflows that run on:
- Pull requests to `main` branch
- Pushes to `main` and `develop` branches

### What Gets Tested
- ✅ Code quality (flake8, black, isort)
- ✅ Security scanning (bandit, safety)
- ✅ Unit tests (pytest)
- ✅ Docker image building
- ✅ Multi-platform compatibility

### Required GitHub Secrets
For deployment, configure these in repository settings:
- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub password
- `OPENAI_API_KEY`: OpenAI API key

## Team Collaboration

### Branch Strategy
```
main              # Production-ready code
├── develop       # Integration branch
├── feature/xyz   # New features
├── fix/abc       # Bug fixes
└── hotfix/123    # Critical production fixes
```

### Pull Request Process
1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit
3. Push branch: `git push origin feature/your-feature`
4. Create PR on GitHub
5. Ensure all CI checks pass
6. Request review from team members
7. Merge after approval

### Code Review Checklist
- [ ] Code follows project style (black formatting)
- [ ] Tests are included for new functionality
- [ ] Documentation is updated if needed
- [ ] Environment variables are properly configured
- [ ] No secrets are committed to code
- [ ] CI pipeline passes

## IDE Configuration

### VS Code (Recommended)
The project includes VS Code configuration:
- `.vscode/settings.json`: Python, linting, formatting settings
- `.vscode/tasks.json`: Common development tasks
- `.vscode/extensions.json`: Recommended extensions

### PyCharm
1. Open project folder
2. Configure Python interpreter: `./venv/bin/python`
3. Install requirements: `pip install -r requirements.txt`
4. Configure run configuration for FastAPI

### Vim/Neovim
Install language servers:
```bash
pip install python-lsp-server[all]
npm install -g pyright
```

## Debugging

### Local Debugging
```bash
# Run with debugger
python -m debugpy --listen 5678 --wait-for-client -m uvicorn app.main:app --reload

# Or use VS Code's debug configuration
```

### Docker Debugging
```bash
# Access container shell
docker-compose exec web bash

# View logs
docker-compose logs -f web

# Debug specific service
docker-compose run --rm web python -c "import sys; print(sys.path)"
```

## Performance Monitoring

### Local Monitoring
```bash
# Install monitoring tools
pip install fastapi-monitor

# Add to main.py
from fastapi_monitor import monitor
monitor.init_app(app)
```

### Production Monitoring
- Use application performance monitoring (APM) tools
- Set up logging aggregation
- Monitor database performance
- Track API response times

## Database Management

### Development Database
```bash
# Create tables
python -c "
from app.database.config import engine, Base
from app.database.models import *
Base.metadata.create_all(bind=engine)
"

# Reset database
rm medical_ai.db  # SQLite
# or docker-compose restart db  # PostgreSQL
```

### Database Migrations
```bash
# Install Alembic for migrations
pip install alembic

# Initialize migrations
alembic init migrations

# Create migration
alembic revision --autogenerate -m "Add new table"

# Apply migration
alembic upgrade head
```

## Testing Strategy

### Test Types
1. **Unit Tests**: `app/tests/test_*.py`
2. **Integration Tests**: Database and API testing
3. **End-to-End Tests**: Full workflow testing

### Running Tests
```bash
# All tests
pytest app/tests/

# Specific test file
pytest app/tests/test_main.py

# With coverage
pytest app/tests/ --cov=app --cov-report=html

# Parallel testing
pytest app/tests/ -n auto
```

## Deployment

### Staging Deployment
```bash
# Build and test locally
docker build -t customer-agents:staging .
docker run -p 8000:8000 --env-file .env customer-agents:staging

# Deploy to staging
git push origin develop  # Triggers staging deployment
```

### Production Deployment
```bash
# Create release branch
git checkout -b release/v1.0.0
git push origin release/v1.0.0

# After testing, merge to main
git checkout main
git merge release/v1.0.0
git tag v1.0.0
git push origin main --tags  # Triggers production deployment
```

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

#### Docker Issues
```bash
# Clean up containers
docker-compose down -v
docker system prune -f

# Rebuild images
docker-compose build --no-cache
```

#### Database Connection
```bash
# Check database URL
echo $DATABASE_URL

# Test connection
python -c "from app.database.config import engine; print(engine.execute('SELECT 1').scalar())"
```

#### Port Conflicts
```bash
# Check what's using port 8000
lsof -i :8000

# Use different port
uvicorn app.main:app --port 8001
```

## Getting Help

1. **Documentation**: Check README.md and this development guide
2. **Issues**: Search existing GitHub issues
3. **Team Chat**: Use your team's communication platform
4. **Code Review**: Ask team members for help during PR reviews

## Contributing

1. Follow the development workflow outlined above
2. Write tests for new features
3. Update documentation as needed
4. Ensure CI pipeline passes
5. Request code review before merging

---

Happy coding! 🚀