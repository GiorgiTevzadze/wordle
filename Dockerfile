FROM python:3.9.6-slim-buster

WORKDIR /app

RUN apt-get update \
	&& apt-get -y install netcat gcc \
	&& apt-get clean


COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./main.py /app

CMD ["python", "main.py"]