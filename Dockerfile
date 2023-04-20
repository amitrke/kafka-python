FROM python:3.7-alpine
RUN apk add git
WORKDIR /app
CMD tail -f /dev/null