FROM python:3.8.10

ADD app/ app/

RUN pip install -r requirement.txt

CMD ["python", "./app/app.py"]