FROM python:3.7-alpine

COPY ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "app.py"]
