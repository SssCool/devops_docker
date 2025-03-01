## Stage 1
FROM python:3.9 AS builder

WORKDIR /app

COPY app.py .


## Stage 2
FROM python:3.9-alpine AS final

WORKDIR /app

COPY --from=builder /app /app

ENV PYTHONUNBUFFERED=1

VOLUME ["/app/numbers"]

ENTRYPOINT ["python", "app.py"]