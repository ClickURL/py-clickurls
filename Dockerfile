FROM python:3.11.0

WORKDIR /py-clickurl_dcoker_container

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN ln -sf /bin/bash /bin/sh




COPY . .

RUN make roll-migration