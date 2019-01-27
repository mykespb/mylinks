FROM python:3.7-alpine

COPY ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE "5000:5000"
EXPOSE "80:80"

CMD ["python", "app.py"]
