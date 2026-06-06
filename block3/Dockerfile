FROM python:3.14-slim

WORKDIR /code

RUN apt-get update && apt-get install -y curl

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt ./ 

RUN pip install -r requirements.txt
RUN pip install python-dotenv

COPY . . 

EXPOSE 5000

CMD ["flask", "run"]


