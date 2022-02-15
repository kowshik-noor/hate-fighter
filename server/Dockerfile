FROM python:alpine

RUN mkdir /usr/src/app/

WORKDIR /usr/src/app/

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["server.py"]

