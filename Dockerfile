FROM python:3.8.10

COPY app/ app/
COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

CMD ["python", "./app/app.py"]