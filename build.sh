#!/bin/bash

clear

rm requirements.txt

pip freeze >> requirements.txt

# Build the Docker image
docker build -t niceygy/colonyassistant .

# Tag the Docker image (optional)
docker tag niceygy/colonyassistant ghcr.io/niceygy/colonisationassistant:latest

# Push the Docker image to GH registry
docker push ghcr.io/niceygy/colonisationassistant:latest

#Update local container

cd /opt/stacks/elite_apps

docker compose pull

docker compose down

docker compose up -d
