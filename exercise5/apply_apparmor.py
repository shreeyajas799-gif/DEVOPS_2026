
import docker

client = docker.from_env()

print("Building image...")
client.images.build(path=".", tag="flask-apparmor")

print("Starting container...")
container = client.containers.run(
    "flask-apparmor",
    ports={"5000/tcp": 5000},
    detach=True
)

try:
    info = client.api.inspect_container(container.id)
    print("Container:", container.short_id)
    print("Security options:", info["HostConfig"]["SecurityOpt"])
    print("AppArmor profile:", info["AppArmorProfile"])
finally:
    container.stop()
    container.remove()
    print("Container stopped and removed.")
