FROM --platform=linux/amd64 joseluisq/static-web-server:2

ENV SERVER_ROOT=/app
ENV SERVER_PORT=3000

WORKDIR /app

COPY ./ui/dist/ ./

EXPOSE 3000
