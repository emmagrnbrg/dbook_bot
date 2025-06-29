FROM python:3.11-slim

RUN mkdir -p /app/logs

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ../admin /app/

RUN mkdir -p /app/logs

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "admin.asgi:application", "--bind", "0.0.0.0:8000"]
