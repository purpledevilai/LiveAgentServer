#!/bin/bash


# Docker run
docker run -p 8080:8080 \
  --name live-agent-server-container \
  -it \
  --env-file .env \
  -e PYTHONUNBUFFERED=1 \
  -v $(pwd)/src:/app \
  live-agent-server-image