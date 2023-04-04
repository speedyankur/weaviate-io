#!/bin/bash

echo "Run Docker compose"
nohup docker-compose -f ./test/docker-compose.yml up -d
