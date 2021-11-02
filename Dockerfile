# syntax=docker/dockerfile:1

#Install Python
FROM python:3.8-slim-buster

RUN pip install pipenv

# Install application into container
COPY . /app

WORKDIR /app


#Run PIPENV
RUN pipenv install --deploy --system --ignore-pipfile


#Run the application
CMD [ "python3", "./run.py"]

