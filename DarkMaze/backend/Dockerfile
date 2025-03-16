# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]
