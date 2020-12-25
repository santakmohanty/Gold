#!/bin/bash

source deactivate
cd /opt/edugem/apps/project
kill -9 $(lsof -ti tcp:8080)
http-server
