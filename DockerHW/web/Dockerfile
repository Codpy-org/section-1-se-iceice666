FROM python:3.11-slim

WORKDIR /app

COPY web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web/ .

EXPOSE 5000

CMD ["python", "main.py"]
