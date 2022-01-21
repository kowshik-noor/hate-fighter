FROM python:alpine

RUN mkdir /usr/src/app/

WORKDIR /usr/src/app/

RUN apk add --update --no-cache supervisor g++ gcc libxslt-dev libffi-dev

COPY . .

ENV C_FORCE_ROOT=1

EXPOSE 5000

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install cryptography

CMD ["/usr/bin/supervisord"]

