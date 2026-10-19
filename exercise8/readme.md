# Exercise 8: Creating a Hello World Jenkins Job

## Objective

To understand Continuous Integration (CI), create a simple shell script, store it in GitHub, and execute it using a Jenkins Freestyle project.

## Tools and Technologies

- **Jenkins:** Automation server for running build jobs.
- **Docker:** Runs Jenkins in a container.
- **Git and GitHub:** Version control and source code hosting.
- **Shell Scripting:** Executes the Hello World script.
- **macOS:** Local development environment.

## Project Structure

```text
DEVOPS_2026/
└── exercise8/
    ├── README.md
    └── hello-world.sh
```

## Step 1: Create the Shell Script

Create a file named `hello-world.sh` with the following content:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

Make the script executable:

```bash
chmod +x hello-world.sh
```

## Step 2: Push the Script to GitHub

The script is stored in the `exercise8` directory of the `DEVOPS_2026` repository.

Run the following commands from the repository root:

```bash
git add exercise8/
git commit -m "Add Exercise 8 Hello World Jenkins job"
git push origin main
```

## Step 3: Configure Jenkins

1. Open Jenkins at `http://localhost:8080`.
2. Create a new item named `HelloWorld1`.
3. Select **Freestyle project**.
4. Under **Source Code Management**, select **Git**.
5. Enter the repository URL:

   `https://github.com/shreeyajas799-gif/DEVOPS_2026`

6. Set the branch specifier to `*/main`.
7. Under **Build Steps**, select **Execute shell**.
8. Enter the following command:

```bash
sh exercise8/hello-world.sh
```

9. Click **Save**.

## Step 4: Run the Jenkins Job

1. Open the `HelloWorld1` job.
2. Click **Build Now**.
3. Open the latest build number.
4. Click **Console Output** to view the execution logs.

## Expected Output

```text
Hello, Jenkins!
Finished: SUCCESS
```

The build should finish successfully when Jenkins can find and execute `exercise8/hello-world.sh`.

## Step 5: Verify the Result

- Confirm that `hello-world.sh` is present in the `exercise8` folder on GitHub.
- Confirm that Jenkins checks out the `main` branch.
- Verify that the console output displays `Hello, Jenkins!`.
- Verify that the build status is `SUCCESS`.

## Conclusion

This exercise demonstrates how to create a shell script, store it in GitHub, configure a Jenkins Freestyle project, and execute the script through a Jenkins build job. It introduces the basic workflow of Continuous Integration and automated task execution.
