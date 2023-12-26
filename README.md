# homekit-logger

## Goal of the project

I wanted a simple API which I can call through HomeKit automation. It logs the event when my front door opens or closes.

## Usage

Set door open status: `curl -X POST 127.0.0.1:8321/status -H 'status: open'`

Set door closed status: `curl -X POST 127.0.0.1:8321/status -H 'status: closed'`

Reset door status: `curl -X POST 127.0.0.1:8321/status -H 'status: unknown'`

Get current door status: `curl -X GET 127.0.0.1:8321/status`

Get container health status: `curl -X GET 127.0.0.1:8321/health`
