#!/bin/bash

docker compose down
docker rmi scientifiks:1.0
docker compose up -d
docker compose logs -f