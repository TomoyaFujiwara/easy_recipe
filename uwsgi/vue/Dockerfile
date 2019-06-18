FROM node:8.15.0-alpine

WORKDIR /app
COPY ./app ./

RUN apk update && \
    npm install && \
    npm install -g npm && \
    npm install -g @vue/cli