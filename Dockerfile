FROM python:3.9.7-slim

WORKDIR /app

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "echo", "Dev environment ready!"]