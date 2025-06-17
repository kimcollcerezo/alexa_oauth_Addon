FROM python:3.11-slim

WORKDIR /app

# Copiem només el run.py
COPY run.py .

# Instal·lem Flask
RUN pip install --no-cache flask

# Cap a executar
CMD ["python", "run.py"]
