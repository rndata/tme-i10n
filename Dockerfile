FROM python:3.8-slim

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . /app
WORKDIR /app
RUN pip install -e .
VOLUME /var/lz-bot

CMD lz-bot run /var/lz-bot/state.pickle
