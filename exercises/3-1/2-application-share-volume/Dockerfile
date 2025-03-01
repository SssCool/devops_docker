FROM python:3.9

WORKDIR /app

COPY app.py .

VOLUME ["/app/numbers"]

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "app.py"]