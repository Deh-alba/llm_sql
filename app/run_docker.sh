#!/bin/bash

docker build -t sql_agent . && docker run -i -t -v "$(pwd)"/:/usr/src/project -p 0.0.0.0:8195:8080 -it sql_agent

#docker run -i -t -v "$(pwd)"/:/usr/src/project -p 0.0.0.0:8190:8080 -it revolve_assistent