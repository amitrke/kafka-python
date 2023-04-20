FROM python:3.7-alpine
RUN apk add git busybox-extras
WORKDIR /app
CMD tail -f /dev/null