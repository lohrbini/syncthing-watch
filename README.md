# Syncthing watch

## About

this repository contains a little python script to monitor the connection state on a syncthing instance

## Build / Installation

```bash
docker build -t syncthing-watch .
```

## docker-compose

```docker-compose
version: "3.9"
services:
  syncthing_check:
    image: syncthing-watch
    restart: always
    environment:
      SYNCTHING_URL: syncthing.example.org
      SYNCTHING_API_TOKEN: 
      PUSHOVER_APP_TOKEN: 
      PUSHOVER_USER_TOKEN: 
      NOTIFICATION_INTERVAL: 60
```

## Run

```
docker-compose up -d
```