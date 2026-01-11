FROM python:3.11-slim

WORKDIR /usr/src/scripts

COPY entrypoint.sh entrypoint.sh
COPY limit_resources.py limit_resources.py
RUN chmod +x ./entrypoint.sh


ENTRYPOINT ["./entrypoint.sh"]
