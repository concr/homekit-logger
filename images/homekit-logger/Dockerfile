FROM alpine:3

WORKDIR /app

COPY homekit-logger.py /app

RUN apk add --update --no-cache curl py3-flask tini && \
    mkdir -vp /app/log

VOLUME ["/app/log"]

EXPOSE 9009/tcp

ENTRYPOINT ["tini","--"]
CMD ["python3","/app/homekit-logger.py","9009"]
