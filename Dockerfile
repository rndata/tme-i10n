FROM python:3.7-slim

ADD requirements.txt /tmp/requirements.txt

RUN tail -n +9 /tmp/requirements.txt > /tmp/requirements-cut.txt &&\
    pip install -r /tmp/requirements-cut.txt

ADD sodeep /deps/sodeep
RUN pip install -e /deps/sodeep

ADD . /app
WORKDIR /app
RUN pip install -e .
VOLUME /var/lz-bot

CMD lz-bot run ckpt
