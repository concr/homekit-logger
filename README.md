# homekit-logger

## Goal of the project

I wanted a simple API which I can call through HomeKit automation, when my front door opens or closes it logs the event.

## Usage

Set open status: `curl -X POST 127.0.0.1:8321/status -H 'status: open'`

Set closed status: `curl -X POST 127.0.0.1:8321/status -H 'status: closed'`

Get current status: `curl -X GET 127.0.0.1:8321/status`

Get health status: `curl -X GET 127.0.0.1:8321/health`
