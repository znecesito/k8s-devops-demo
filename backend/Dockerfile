FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV APP_VERSION=dev
CMD ["python", "app.py"]
