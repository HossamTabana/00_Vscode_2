# Docker and Docker-Compose Cheat Sheet

This document provides a list of commonly used Docker and Docker-Compose commands.

## Docker Commands

### 1. `docker --version`
- **Explanation**: Displays the installed Docker version.
- **Example**: `docker --version`

### 2. `docker info`
- **Explanation**: Shows system-wide information about Docker and its components.
- **Example**: `docker info`

### 3. `docker pull`
- **Explanation**: Downloads an image from Docker Hub or another registry.
- **Example**: `docker pull ubuntu`

### 4. `docker build`
- **Explanation**: Builds a Docker image from a Dockerfile.
- **Example**: `docker build -t my-image:latest .`

### 5. `docker images`
- **Explanation**: Lists all locally stored Docker images.
- **Example**: `docker images`

### 6. `docker rmi`
- **Explanation**: Removes one or more Docker images.
- **Example**: `docker rmi my-image:latest`

### 7. `docker ps`
- **Explanation**: Lists running containers.
- **Example**: `docker ps`

### 8. `docker ps -a`
- **Explanation**: Lists all containers, both running and stopped.
- **Example**: `docker ps -a`

### 9. `docker run`
- **Explanation**: Creates and starts a container from an image.
- **Example**: `docker run -d --name my-container ubuntu`

### 10. `docker exec`
- **Explanation**: Runs a command in a running container.
- **Example**: `docker exec my-container ls`

### 11. `docker stop`
- **Explanation**: Stops one or more running containers.
- **Example**: `docker stop my-container`

### 12. `docker start`
- **Explanation**: Starts one or more stopped containers.
- **Example**: `docker start my-container`

### 13. `docker rm`
- **Explanation**: Removes one or more containers.
- **Example**: `docker rm my-container`

### 14. `docker logs`
- **Explanation**: Fetches the logs of a container.
- **Example**: `docker logs my-container`

### 15. `docker inspect`
- **Explanation**: Shows detailed information in JSON format.
- **Example**: `docker inspect my-container`

### 16. `docker network ls`
- **Explanation**: Lists all Docker networks.
- **Example**: `docker network ls`

### 17. `docker volume ls`
- **Explanation**: Lists all Docker volumes.
- **Example**: `docker volume ls`

### 18. `docker port`
- **Explanation**: Lists port mappings for a container.
- **Example**: `docker port my-container`

### 19. `docker top`
- **Explanation**: Displays the running processes in a container.
- **Example**: `docker top my-container`

### 20. `docker stats`
- **Explanation**: Shows real-time resource usage statistics.
- **Example**: `docker stats`

### 21. `docker commit`
- **Explanation**: Creates a new image from a container's changes.
- **Example**: `docker commit my-container my-new-image:latest`

### 22. `docker tag`
- **Explanation**: Assigns a tag to an image, useful for versioning.
- **Example**: `docker tag my-image:latest my-image:v1`

### 23. `docker push`
- **Explanation**: Pushes an image to a registry like Docker Hub.
- **Example**: `docker push my-image:latest`

### 24. `docker search`
- **Explanation**: Searches for images on Docker Hub or another registry.
- **Example**: `docker search ubuntu`

### 25. `docker login`
- **Explanation**: Logs in to a Docker registry, like Docker Hub.
- **Example**: `docker login`

### 26. `docker logout`
- **Explanation**: Logs out from a Docker registry.
- **Example**: `docker logout`

### 27. `docker save`
- **Explanation**: Saves an image to a TAR archive.
- **Example**: `docker save -o my-image.tar my-image:latest`

### 28. `docker load`
- **Explanation**: Loads an image from a TAR archive.
- **Example**: `docker load -i my-image.tar`

### 29. `docker cp`
- **Explanation**: Copies files or directories between a container and the local filesystem.
- **Example**: `docker cp my-container:/file.txt ./file.txt`

### 30. `docker-compose up`
- **Explanation**: Builds, (re)creates, starts, and attaches to containers for services defined in a `docker-compose.yaml` file.
- **Example**: `docker-compose up`

### 31. `docker-compose down`
- **Explanation**: Stops and removes all containers defined in the `docker-compose.yaml` file.
- **Example**: `docker-compose down`

### 32. `docker-compose ps`
- **Explanation**: Lists all running services defined in `docker-compose.yaml`.
- **Example**: `docker-compose ps`

### 33. `docker-compose logs`
- **Explanation**: View the logs for a service.
- **Example**: `docker-compose logs <service_name>`

### 34. `docker-compose start`
- **Explanation**: Starts existing containers for a service.
- **Example**: `docker-compose start <service_name>`

### 35. `docker-compose stop`
- **Explanation**: Stops running containers without removing them.
- **Example**: `docker-compose stop <service_name>`

### 36. `docker-compose restart`
- **Explanation**: Restarts all stopped and running services.
- **Example**: `docker-compose restart`

### 37. `docker-compose build`
- **Explanation**: Builds all services defined in `docker-compose.yaml`.
- **Example**: `docker-compose build`

### 38. `docker-compose config`
- **Explanation**: Validates and shows the `docker-compose.yaml` configuration.
- **Example**: `docker-compose config`

### 39. `docker-compose pull`
- **Explanation**: Pulls the latest version of an image.
- **Example**: `docker-compose pull <service_name>`

### 40. `docker-compose run`
- **Explanation**: Runs a one-time command for a service. Useful for debugging.
- **Example**: `docker-compose run <service_name> <command>`

## Conclusion

This cheat sheet covers basic Docker and Docker-Compose commands to help you manage your containers and services. Save this document for future reference.
