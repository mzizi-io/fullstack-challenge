# WDTech Challenge
This is a simple implementation of the FastAPI Backend and Vue front end. I have given a number of justifications for some of the decisions made in the DISCLAIMERS section.

I also note that there are possibly a few (to quite a number) of errors and these will likely be due to an oversight on my part. I keep my fingers very crossed that there are no architectural errors, however!

## Running the backend app locally (without Docker)

To run the app, follow the following steps:

1. Ensure you have Python 3 installed
2. Run `pip install pipenv` to install `pipenv` which will manage dependencies
3. Run `pipenv install` to install dependencies
4. Run `pipenv shell` to activate your virtual environment
5. Run `py -m src.main` or `python -m src.main` depending on the version of python you have
6. You can also run `pipenv run py -m src.main` if you do not want to activate the virtual environment with `pipenv shell`

## Running the frontend app locally (without Docker)

1. Ensure you have npm installed
2. Run `npm install` 
3. Run `npm run dev`

## Running the apps locally (with Docker)
I have created a `docker-compose.yml` file at the root of the main repository and have made justifications for this there.

To run this run `docker compose up`

# Pre Commit
I've noted that code standards and technical debt are never a big change but the result of multiple small things that add up.

I think pre-commit is a great addition to ensuring well written, properly formatted code.

# CI Pipeline
To run the tests and flake8 on the CI pipeline, run: ```docker-compose -f docker-compose-ci.yml up --build --abort-on-container-exit```

# Tox (CI Pipeline locally)
This is entirely for use in the CI pipeline. This should run all the tests and linting.

To run this locally:

1. Run `tox` on the command line

# DISCLAIMERS

1. I think I probably should have picked a simpler db but the idea is also to challenge oneself and I do feel like Postgres is perfect for full text search because of the indexing capabilities
2. I really havent had time to write tests or documentation with pytest and mkdocs respectively but I will try and implement this today but if not possible hopefully this suffices