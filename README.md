# homekit-logger

## Goal of the project

I wanted a simple API which I can call through HomeKit automation. It logs the event when my front door opens or closes.

## Usage

Set open status: `curl -X POST 127.0.0.1:8321/status -H 'status: open'`

Set closed status: `curl -X POST 127.0.0.1:8321/status -H 'status: closed'`

Reset status: `curl -X POST 127.0.0.1:8321/status -H 'status: unknown'`

Get current status: `curl -X GET 127.0.0.1:8321/status`

Get health status: `curl -X GET 127.0.0.1:8321/health`
