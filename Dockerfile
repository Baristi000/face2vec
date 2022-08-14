FROM tensorflow/tensorflow:latest-devel-gpu

COPY . /app
WORKDIR /app

RUN apt update &&\
    apt install curl cmake -y

RUN pip install --upgrade pip setuptools &&\
    pip install -r resources/requirements.txt

CMD python main.py
