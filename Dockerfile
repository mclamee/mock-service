FROM node:16-alpine3.11

WORKDIR /app

ADD . /app

RUN npm install -g mockserver

ENTRYPOINT ["mockserver", "-p", "8080", "-m", "mocks"]

