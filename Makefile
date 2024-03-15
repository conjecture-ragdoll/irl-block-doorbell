
DOCKER_IMAGE_NAME = doorbell
DOCKER_CONTAINER_NAME = doorbell-container

# Build Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run Docker container
run:
	docker run -d -p 8000:8000 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Stop Docker container
stop:
	docker stop $(DOCKER_CONTAINER_NAME)

# Remove Docker container
remove:
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up Docker environment
clean: stop remove

# Help
help:
	@echo "Available commands:"
	@echo "  make build       - Build Docker image"
	@echo "  make run         - Run Docker container"
	@echo "  make stop        - Stop Docker container"
	@echo "  make remove      - Remove Docker container"
	@echo "  make clean       - Stop and remove Docker container"
	@echo "  make help        - Display this help message"

