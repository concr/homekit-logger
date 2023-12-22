FROM pypy:3-slim

RUN mkdir -p /app/log

WORKDIR /app

COPY homekit-logger.py /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME [ "/app/log" ]

EXPOSE 8321/tcp

CMD [ "pypy3", "/app/homekit-logger.py", "8321" ]