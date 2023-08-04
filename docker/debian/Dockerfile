FROM debian:buster-slim

RUN apt-get update
RUN apt-get install -y python3

COPY main.py /app

CMD python3 /app/main.py
