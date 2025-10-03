# homekit-logger

## Goal of the project

I wanted a simple API which I can call through HomeKit automation. It logs the event when my front door opens or closes.

## Prerequisited

* HomeKit hub like an AppleTV or HomePod
* HomeKit compatible door sensor like "Eve Door & Window"
* Something like a home server, or Raspberry Pi in the same network where you can run Docker containers

## Makefile

Ignore the Makefile, it's for my personal use.

## Setup container

The container should run on a system, which can be reached by your HomeKit hub.

Just start the container with `docker compose up -d --build` and go on to the next part.

## Setup automation for logging

TBD: Changed in iOS 26 a bit ...

* Open Home app (iOS, iPadOS or macOS)
* Click `+` then `Add Automation`
* Select `A Sensor Detects Something`
* Select your door sensor and click `Next`
* Choose "When" state (Opens, Closes, Time, People)
* Scroll down to `Convert To Shortcut` and click it
* Remove `Set Scenes and Accessories` with the `X`
* Click `Add Action` and search for `contents`
* Select the `Get Contents of URL`
* Click the `URL` field and enter `YOUR_SERVER_IP:8321/status`
* Open up the advanced settings with the arrow down icon
* Change `Method` to `POST`
* Add an header: Key `status` Text `open` or `closed`
* Click `Next` then `Test This Automation`
* Your event should be logged in the logfile `volumes/homekit-logger/log/homekit-logger.log`
* Finally click `Done`

## Manually API usage

Set door open status: `curl -X POST 127.0.0.1:8321/status -H 'status: open'`

Set door closed status: `curl -X POST 127.0.0.1:8321/status -H 'status: close'`

Reset door status: `curl -X POST 127.0.0.1:8321/status -H 'status: unknown'`

Get current door status: `curl -X GET 127.0.0.1:8321/status`

Get container health status: `curl -X GET 127.0.0.1:8321/health`
