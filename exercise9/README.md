cat > ../README.md <<'EOF'
# Jenkins Multi-Stage Pipeline: Python Flask Application

## Objective
Automate building, code-quality checks, testing, and deployment of a Flask application using Jenkins.

## Pipeline Stages
1. Build - Create a Python virtual environment and install dependencies.
2. Code Quality - Run Flake8.
3. Test - Execute unit tests.
4. Deploy - Copy application files to a deployment directory.
5. Run Application - Start the Flask application.
6. Test Application - Run application tests.

## Technologies
- Python
- Flask
- Jenkins
- Git and GitHub
- Flake8

## Expected Result
The Jenkins pipeline completes successfully when dependency installation,
code-quality checks, unit tests, and deployment steps pass.
EOF