#!/bin/sh

docker build -t gcr.io/rndata/lz-bot:latest .
docker push gcr.io/rndata/lz-bot
