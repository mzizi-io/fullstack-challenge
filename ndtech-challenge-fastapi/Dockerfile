FROM python:3.11-slim

RUN apt-get update && apt-get install -y postgresql-client

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --deploy --system --ignore-pipfile

COPY . .

CMD ["sh", "./scripts/run.sh"]