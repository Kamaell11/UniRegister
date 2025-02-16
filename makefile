# Description: Makefile for UniRegisterApp project
APP_NAME = UniRegisterApp
DOCKER_IMAGE = uniregister_app

# Install dependencies in the virtual environment
install:
		pip install -r requirements.txt

# Run the application locally (outside Docker)
run:
		python main.py

# Build Docker image
docker_build:
		docker build -t $(DOCKER_IMAGE) .

# Run Docker container with necessary environment variables for display
docker_run:
		# Run the Docker container with DISPLAY environment variable
		docker run --rm -it \
		-e DISPLAY=$$DISPLAY \
		-v /tmp/.X11-unix:/tmp/.X11-unix \
		$(DOCKER_IMAGE)

# Remove Docker image and containers after testing
docker_clean:
		# Remove the existing image
		docker rmi -f $(DOCKER_IMAGE)

# Run application in Docker container
docker:
		# Build the Docker image and run the container
		$(MAKE) docker_build
		$(MAKE) docker_run
