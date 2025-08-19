#!/bin/bash

# Validation script to check if the remote development setup is complete
echo "🔍 Validating Customer Agents Remote Development Setup"
echo "=================================================="

# Check if required files exist
files=(
    "README.md"
    "requirements.txt" 
    "requirements-dev.txt"
    ".env.example"
    "Dockerfile"
    "docker-compose.yml"
    "setup.sh"
    "quick-start.sh"
    ".github/workflows/ci-cd.yml"
    "app/main.py"
    "app/agents/agent_manager.py"
    "app/routes/auth.py"
    "app/tests/test_main.py"
    ".vscode/settings.json"
    "DEVELOPMENT.md"
)

echo "📁 Checking required files..."
missing_files=0
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file (missing)"
        missing_files=$((missing_files + 1))
    fi
done

echo ""
echo "📋 Checking file permissions..."
if [ -x "setup.sh" ]; then
    echo "✅ setup.sh is executable"
else
    echo "❌ setup.sh is not executable"
    missing_files=$((missing_files + 1))
fi

if [ -x "quick-start.sh" ]; then
    echo "✅ quick-start.sh is executable"
else
    echo "❌ quick-start.sh is not executable"
    missing_files=$((missing_files + 1))
fi

echo ""
echo "🔧 Checking configuration files..."

# Check if .env.example has required variables
required_vars=("OPENAI_API_KEY" "DATABASE_URL" "JWT_SECRET")
for var in "${required_vars[@]}"; do
    if grep -q "$var" ".env.example" 2>/dev/null; then
        echo "✅ .env.example contains $var"
    else
        echo "❌ .env.example missing $var"
        missing_files=$((missing_files + 1))
    fi
done

echo ""
echo "🐳 Checking Docker configuration..."

# Check if Dockerfile has proper structure
if grep -q "FROM python" "Dockerfile" 2>/dev/null; then
    echo "✅ Dockerfile has Python base image"
else
    echo "❌ Dockerfile missing or invalid"
    missing_files=$((missing_files + 1))
fi

if grep -q "fastapi" "docker-compose.yml" 2>/dev/null || grep -q "web:" "docker-compose.yml" 2>/dev/null; then
    echo "✅ docker-compose.yml configured for web service"
else
    echo "❌ docker-compose.yml missing or invalid"
    missing_files=$((missing_files + 1))
fi

echo ""
echo "🧪 Checking test structure..."
if [ -d "app/tests" ] && [ -f "app/tests/test_main.py" ]; then
    echo "✅ Test structure is set up"
else
    echo "❌ Test structure missing"
    missing_files=$((missing_files + 1))
fi

echo ""
echo "⚙️ Checking CI/CD configuration..."
if [ -f ".github/workflows/ci-cd.yml" ]; then
    if grep -q "pytest" ".github/workflows/ci-cd.yml"; then
        echo "✅ CI/CD pipeline includes testing"
    else
        echo "⚠️ CI/CD pipeline exists but may be incomplete"
    fi
else
    echo "❌ CI/CD pipeline missing"
    missing_files=$((missing_files + 1))
fi

echo ""
echo "📝 Summary:"
echo "=========="
if [ $missing_files -eq 0 ]; then
    echo "🎉 All checks passed! The project is ready for remote development."
    echo ""
    echo "🚀 Next steps:"
    echo "   1. Run './quick-start.sh' to start development"
    echo "   2. Copy '.env.example' to '.env' and configure your API keys"
    echo "   3. Choose Docker or local development based on your preference"
    echo "   4. Read DEVELOPMENT.md for detailed team collaboration guidelines"
    echo ""
    echo "✅ Remote development setup is COMPLETE!"
else
    echo "⚠️ Found $missing_files issues that need attention."
    echo "Please check the items marked with ❌ above."
    exit 1
fi