#!/bin/bash
set -ex
./manage.py collectstatic --no-input
docker buildx build --platform=linux/amd64,linux/arm64 -t holdenk/pcfweb:v0.0.1k . --push

