FROM tensorflow/tensorflow:latest-devel-gpu

COPY . .

RUN apt update &&\
    apt install cmake -y

RUN pip install --upgrade pip setuptools &&\
    pip install -r resources/requirements.txt

CMD python main.py