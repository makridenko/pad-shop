#!/bin/bash

# Build web client
docker-compose up -d --build webclient
docker exec pad-shop_webclient_1 yarn install
docker exec pad-shop_webclient_1 yarn build
docker-compose down

rm -rf kernel/webclient
cp -r client/build kernel/webclient
rm -rf client/build

docker-compose up -d --build nginx