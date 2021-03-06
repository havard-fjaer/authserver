FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y curl
COPY . .

#CMD [ "python3", "app.py"]

ENTRYPOINT [ "python3", "server.py"]
