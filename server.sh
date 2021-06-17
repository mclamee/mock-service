#!/bin/sh
docker run -it --rm --init -p 8080:8080 -v `pwd`/mocks:/app/mocks mockserver:latest
