FROM alpine:latest

RUN apk add --no-cache bash python3 py3-pip

COPY run.py /run.py
RUN pip3 install flask

CMD ["python3", "/run.py"]
