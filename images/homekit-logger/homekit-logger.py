#!/usr/bin/env python3

import json
import sys
import logging
from flask import Flask, Response, request

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('/app/log/homekit-logger.log')
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

logger = setup_logger()

app = Flask(__name__)

door_status = "unknown"
door_status_json = {"status": door_status}

@app.route("/")
def main():
    return Response(status=204)

@app.route("/status", methods=['GET'])
def status():
    return Response(
        response=json.dumps(door_status_json),
        status=200,
        mimetype="application/json"
    )

@app.route("/status", methods=['POST'])
def set_status():
    global door_status, door_status_json
    status_header = request.headers.get('status')

    if status_header not in ["open", "closed", "unknown"]:
        return Response(
            response=json.dumps({"error": "Invalid state"}),
            status=400,
            mimetype="application/json"
        )

    door_status = status_header
    door_status_json["status"] = door_status
    logger.info(f"door_{door_status}")
    return Response(
        response=json.dumps(door_status_json),
        status=200,
        mimetype="application/json"
    )

@app.route("/health", methods=['GET'])
def health():
    return Response(
        response="OK",
        status=200,
        mimetype="text/plain "
    )


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    try:
        app.run('0.0.0.0', port)
    except Exception as e:
        logger.error(f"Failed to start Flask app: {e}")
