FROM ubuntu:latest

WORKDIR /app

RUN apt update && \
	apt upgrade -y && \
    apt install -y python3.10 pip xvfb wget

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install ./google-chrome-stable_current_amd64.deb -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD xvfb-run python3 client.py
