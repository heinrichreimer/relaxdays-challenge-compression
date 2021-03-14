FROM python:3.8

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

COPY . /app/

ENTRYPOINT ["python", "/app/main.py"]
