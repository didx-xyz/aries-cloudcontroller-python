#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

CONTAINER_NAME=openapi-converter

# The ulimit flag below is for "library initialization failed - unable to allocate file descriptor table - out of memory" 
# error from docker logs. 
${CONTAINER_RUNTIME} run --rm -d -p 8080:8080 --ulimit nofile=8096:8096 --name ${CONTAINER_NAME} swaggerapi/swagger-converter:v1.0.5
trap '${CONTAINER_RUNTIME} stop ${CONTAINER_NAME}' EXIT
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8080)" != "200" ]];do
    echo "Converter not yet ready..."
    sleep 1
done

curl -X POST http://localhost:8080/api/convert -H "Content-Type: application/json" -H "Accept: application/yaml" --data-binary "@../data/swagger.json" -o ../data/openapi.yml
