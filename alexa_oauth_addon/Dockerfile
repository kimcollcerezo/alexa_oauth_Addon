FROM alpine:latest

# Afegim Python, pip i dependències de compilació per a MarkupSafe, etc.
RUN apk add --no-cache \
      bash \
      python3 \
      py3-pip \
      build-base \
      libffi-dev \
      openssl-dev

COPY run.py /run.py

# Instal·lem Flask
RUN pip3 install --no-cache-dir flask

CMD ["python3", "/run.py"]
