FROM python:3.11.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0"]
