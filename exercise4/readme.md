
# Exercise 4: Docker Networking with Multiple Containers

## Objective
Understand Docker bridge networking and communication between multiple containers.

## Technologies Used
- Docker
- Python
- Flask
- MySQL
- Redis

## Tasks Performed
1. Created a custom bridge network named `my-bridge-net`.
2. Built a Flask REST API Docker image.
3. Launched Flask, MySQL, and Redis containers on the same network.
4. Exposed Flask on host port 5001.
5. Tested the Flask API and container name resolution.
6. Removed containers and the bridge network during cleanup.

## API Endpoint
`GET /about`

URL: `http://localhost:5001/about`

## Key Learnings
- Containers on the same user-defined bridge network can communicate using container names.
- The `-p` flag maps a container port to a host port.
- Bridge networks provide network isolation from unrelated containers.

## Cleanup
```bash
docker stop mysql redis flask
docker rm mysql redis flask
docker network rm my-bridge-net
```
