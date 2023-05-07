FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

COPY /data /data
RUN apt install -y python3-tk
RUN pip3 install -r requirements.txt

COPY . .
