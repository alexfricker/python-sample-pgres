# Sample Postgres Python Operations
A starter project for manipulating data in Postgres using the python [`psycopg2`](https://www.psycopg.org/doc) library.

## Postgres Installation
A docker-compose file is included which can create a local instance of postgres. This will create a default user and database of `postgres` with the password specified in `POSTGRES_PASSWORD`. If you already have an instance of postgres running, you can ignore this file.

To install postgres using the supplied docker file, first make sure docker is installed on your machine ([see docker docs](https://docs.docker.com/engine/install/)) and then run `docker compose up` or `docker-compose up`.

## Environment Setup
Create a virtual environment with python and install requirements (be sure to change directory [cd] to the location you cloned the repo..). This will depend slightly on your os and setup but should be similar to:

### Create VENV:

`python` or `python3 -m venv .venv`

### Activate VENV:
- Windows - `.venv\bin\Activate.ps1`
- Mac - `source .venv/bin/activate`

### Install reqs:
`pip install -r requirements.txt`

## Environment Variables
Connection settings for postgres are located within the `settings.py` file and should be modified as required. Either create environment variables for each of the entries on your machine, or replace the existing code with strings for your specific database instance:

`"DB_NAME": "postgres"`

`"DB_HOST": "YOUR_SERVER_NAME"`

etc...

_friendly reminder not to commit or save sensitive config values :)_

If you are using the docker-compose file to create a postgres instance, the settings file is already configured to use the appropriate default values.

## Running code samples
The `main.py` file contains a handful of basic samples for connecting to the database and running queries. Feel free to adjust the function calls to suit your testing needs.