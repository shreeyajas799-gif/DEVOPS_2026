# Introduction to Continuous Integration (CI) and Jenkins Installation

## Objective

To understand Continuous Integration (CI), learn about Jenkins, and install and configure Jenkins using Docker.

## 1. What is Continuous Integration (CI)?

Continuous Integration is a software development practice in which developers frequently integrate their code changes into a shared repository. Automated builds and tests help identify errors early and improve software quality.

### Key Features of CI
- **Frequent Integration:** Developers regularly commit and push code.
- **Automated Builds:** Code changes trigger automated build processes.
- **Automated Testing:** Tests check whether the application works correctly.
- **Immediate Feedback:** Developers receive build and test results quickly.

### Benefits of CI
- Early detection of bugs.
- Improved team collaboration.
- Faster development cycles.
- Better software quality.
- Reduced integration problems.

## 2. What is Jenkins?

Jenkins is an open-source automation server used to automate software building, testing, and deployment. It supports Continuous Integration (CI) and Continuous Delivery (CD) through pipelines and plugins.

### Key Jenkins Concepts
1. **Job:** A task configured to run in Jenkins.
2. **Build:** An execution of a job.
3. **Pipeline:** A sequence of automated build, test, and deployment steps.
4. **Plugins:** Extensions that add functionality to Jenkins.
5. **Nodes:** Machines that execute Jenkins tasks.

## 3. Prerequisites

- macOS
- Docker Desktop installed and running
- Internet connection
- Web browser

## 4. Install Jenkins Using Docker

Run the following command to download the Jenkins LTS image and start a container:

```bash
docker run -d --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  jenkins/jenkins:lts
```

### Explanation

- `-d`: Runs the container in the background.
- `--name jenkins`: Assigns the container the name `jenkins`.
- `-p 8080:8080`: Maps Jenkins' web interface port to the host.
- `-p 50000:50000`: Maps the port commonly used for inbound agent connections.
- `jenkins/jenkins:lts`: Uses the Jenkins Long-Term Support Docker image.

## 5. Verify the Jenkins Container

Check whether Jenkins is running:

```bash
docker ps
```

To view the Jenkins container logs:

```bash
docker logs jenkins
```

## 6. Retrieve the Initial Administrator Password

Run:

```bash
docker exec jenkins \
  cat /var/jenkins_home/secrets/initialAdminPassword
```

Copy the generated password for the initial setup.

## 7. Access Jenkins

Open the following URL in your web browser:

**http://localhost:8080**

Complete the initial configuration:

1. Enter the initial administrator password.
2. Select **Install suggested plugins**.
3. Create an administrator user.
4. Complete the setup and open the Jenkins dashboard.

## 8. Verify the Installation

Jenkins is ready when the dashboard opens successfully in your browser.

You can verify the container status again using:

```bash
docker ps
```

## 9. CI Workflow Using Jenkins

1. A developer writes or modifies code.
2. The code is pushed to a Git repository.
3. Jenkins detects the changes when configured with a suitable trigger.
4. Jenkins runs the configured build and test steps.
5. Jenkins reports whether the pipeline succeeded or failed.

## 10. Common Docker Commands

| Command | Purpose |
|---|---|
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker logs jenkins` | View Jenkins logs |
| `docker start jenkins` | Start an existing stopped container |
| `docker stop jenkins` | Stop Jenkins |
| `docker restart jenkins` | Restart Jenkins |
| `docker exec -it jenkins bash` | Open a shell inside the container |

## 11. Conclusion

In this exercise, Continuous Integration and its benefits were studied, and Jenkins was installed using Docker. The Jenkins container was verified, the initial administrator password was retrieved, and the web interface was accessed through port 8080.

Jenkins can now be used to create jobs and pipelines that automate software build and testing workflows.

## References

- [Jenkins Official Website](https://www.jenkins.io/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Jenkins Docker Image](https://hub.docker.com/r/jenkins/jenkins)
