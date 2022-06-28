FROM python:alpine

RUN pip3 install requests urllib3 python-http-client

WORKDIR /app

COPY syncthing.py syncthing.py

CMD ["python3", "syncthing.py"]