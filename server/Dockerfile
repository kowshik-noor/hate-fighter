FROM python:alpine

RUN mkdir /usr/src/app/

WORKDIR /usr/src/app/

COPY . .

EXPOSE 5000

RUN apk add --update --no-cache g++ gcc libxslt-dev libffi-dev
RUN pip install cryptography
RUN apk del libffi-dev libxslt-dev


RUN pip install -r requirements.txt gunicorn


ENTRYPOINT [ "gunicorn" ]

CMD ["--bind", "0.0.0.0:5000", "wsgi:application"]

