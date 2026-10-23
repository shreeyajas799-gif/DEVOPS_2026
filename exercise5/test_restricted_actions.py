
import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    command=["python", "-c", "import time; time.sleep(300)"]
)

try:
    for command in [
        ["cat", "/etc/passwd"],
        ["/bin/bash", "-c", "echo shell executed"]
    ]:
        result = container.exec_run(command)
        print("Command:", command)
        print("Exit code:", result.exit_code)
        print("Output:", result.output.decode(errors="replace"))
finally:
    container.stop()
    container.remove()
