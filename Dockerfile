FROM python:3.13

WORKDIR /app

COPY app.py requirements.txt .env ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:15666", "app:app"]
