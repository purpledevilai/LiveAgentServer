#!/bin/bash


# Docker run
docker run -p 9000:9000 \
  --name chat-stream-server-container \
  -it \
  --env-file .env \
  -e PYTHONUNBUFFERED=1 \
  -v $(pwd)/src:/app \
  chat-stream-server-image