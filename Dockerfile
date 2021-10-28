# syntax=docker/dockerfile:1

#Install Python
FROM python:3.8-slim-buster

RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .

#Run PIPENV
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


# Install application into container
COPY . .

#Run the application
CMD [ "python3", "run.py"]

