FROM alpine:3.19

WORKDIR /app

COPY homekit-logger.py /app

RUN apk add --update --no-cache curl py3-flask && \
    mkdir -vp /app/log

VOLUME [ "/app/log" ]

EXPOSE 8321/tcp

CMD [ "python3", "/app/homekit-logger.py", "8321" ]
