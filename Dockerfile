FROM python:3.9.9-slim-buster

WORKDIR /codewars

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY scrapper_code.py .

CMD [ "python", "scrapper_code.py" ]