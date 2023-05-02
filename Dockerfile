FROM python:3.8

WORKDIR /sound_recognition

COPY requirements.txt .

RUN pip install -r requirements.text

COPY . ./app

CMD ["python", "./app/app.py"]