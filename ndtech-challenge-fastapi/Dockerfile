FROM python:3.11-slim

RUN apt-get update \
&& apt-get install -y postgresql-client libpq-dev gcc\
&& rm -rf /var/lib/apt/lists

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --deploy --system --ignore-pipfile

COPY . .

CMD ["sh", "./scripts/run.sh"]