FROM python:3.9.5-alpine3.13

#for avoid any printing in the console of the container.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt  /requirements.txt

#Learning contains Django source code.
COPY ./learning /learning 

WORKDIR /learning
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --upgrade --no-cache postgresql-client && \
    apk add --upgrade --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home himanshu && \
    mkdir -P /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R himanshu:himanshu /vol && \
    chmod -R 755 /vol


ENV PATH="/py/bin:$PATH"

USER himanshu
