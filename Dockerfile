FROM python:3.7

COPY ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE "5000:5000"

CMD ["python", "app.py"]
