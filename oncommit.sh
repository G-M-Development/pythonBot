#!/bin/bash

# Define Docker image names
NEW_IMAGE="my-image-name:new"
CURRENT_IMAGE="my-image-name:current"
OLD_IMAGE="my-image-name:old"

# Build the new Docker image
docker build -t $NEW_IMAGE .

# Tag the current Docker image as old (if exists)
if docker image inspect $CURRENT_IMAGE > /dev/null 2>&1; then
    docker tag $CURRENT_IMAGE $OLD_IMAGE
fi

# Tag the new Docker image as current
docker tag $NEW_IMAGE $CURRENT_IMAGE

# Remove the old Docker image
if docker image inspect $OLD_IMAGE > /dev/null 2>&1; then
    docker image rm $OLD_IMAGE
fi

# Remove dangling images
docker image prune -f
