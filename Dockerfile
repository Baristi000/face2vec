FROM tensorflow/tensorflow:latest-devel-gpu

COPY . /app
WORKDIR /app

RUN apt update &&\
    apt install curl cmake -y

RUN mkdir -p resources/checkpoints
RUN wget -cO  ./resources/checkpoints/saved.ckpt.index \
    "https://drive.google.com/uc?export=download&id=1cPhel0yn3XVEYrzpo0coGD0Tfv_FKGUy"
RUN wget -cO  ./resources/checkpoints/saved.ckpt.data-00000-of-00001 \
    "https://drive.google.com/uc?export=download&id=1W09EJOxqbdVpXrA-i42au3tQb2KNDR5Z"
RUN pip install --upgrade pip setuptools &&\
    pip install -r resources/requirements.txt

CMD python main.py