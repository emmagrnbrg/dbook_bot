FROM python:3.11

RUN mkdir -p /app/logs

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "Main"]