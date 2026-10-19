# Exercise 9: Jenkins Multi-Stage Pipeline for a Python Flask Application

## Objective

To create and execute a Jenkins Declarative Pipeline that automates building, testing, and deploying a sample Python Flask application.

## Technologies Used

- Jenkins
- Docker
- Python
- Flask
- Git and GitHub
- Jenkins Pipeline

## Project Structure

```text
exercise9/
├── README.md
└── python-flask-app/
    ├── app.py
    ├── requirements.txt
    ├── test_app.py
    └── Jenkinsfile
```

## Pipeline Stages

1. **Build:** Creates a Python virtual environment and installs dependencies.
2. **Test:** Executes automated unit tests using Python's `unittest` framework.
3. **Deploy:** Copies application files to a mock deployment directory.
4. **Run Application:** Starts the Flask application as a background process.
5. **Test Application:** Sends an HTTP request to verify that the application responds correctly.

## Application

The Flask application responds to requests at `/` with:

```text
Hello, Jenkins Multi-Stage Pipeline!
```

## Jenkins Configuration

1. Create a Jenkins Pipeline job named `Python-MultiStage-Pipeline`.
2. Select **Pipeline script from SCM**.
3. Choose Git and provide the `DEVOPS_2026` repository URL.
4. Set the branch to `*/main`.
5. Set the Script Path to:

   `exercise9/python-flask-app/Jenkinsfile`

6. Save the job and click **Build Now**.

## Expected Result

The pipeline should complete the Build, Test, Deploy, Run Application, and Test Application stages successfully.

The final console output should contain:

```text
Hello, Jenkins Multi-Stage Pipeline!
Pipeline completed successfully!
Finished: SUCCESS
```

## Conclusion

This exercise demonstrates how Jenkins automates multiple stages of a software delivery workflow using a Declarative Pipeline. It introduces dependency installation, automated testing, mock deployment, application startup, and HTTP verification.
