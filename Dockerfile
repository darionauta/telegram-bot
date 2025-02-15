FROM python:3.13

WORKDIR /app

COPY main.py requirements.txt .env ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
