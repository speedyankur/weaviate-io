#!/bin/bash

echo "Stop Docker compose"
nohup docker-compose  -f ./test/docker-compose.yml down
