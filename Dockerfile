FROM debian:latest


RUN apt-get update
RUN apt-get install -y python3 python3-pip gunicorn3

COPY app app/

WORKDIR app/

RUN pip3 install -r requirements.txt



CMD ["gunicorn", "-b", "0.0.0.0:8888","entrypoint:app"]