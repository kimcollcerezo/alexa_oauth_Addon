FROM python:3.11-slim
WORKDIR /app
COPY run.py .
RUN pip install flask
CMD ["python", "run.py"]
