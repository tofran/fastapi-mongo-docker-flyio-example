# FastAPI + MongoDB + Docker + Fly.io with CI/CD

This is a very opinionated example repository for a python backend API. It is not a template as it contains a few things already as an example for how to build something from here.

[This project](https://github.com/grillazz/fastapi-mongodb) was originally created by [grillazz](https://github.com/grillazz), this is a hard fork as I intend to deviate from the upstream - adding more opinion and changing a few things.

## Requirements

Before starting the development you must install the following tools on your machine:

- `make`
- `docker` and `docker-compose`

Optionally, if your editor runs in host, you should:

- Create a virtual environment with python 3.10: `python3.10 -m venv env` and activate it with your shell.
- Install the requirements (including the dev ones): `pip install -r requirements-dev.txt`.

# Development

Just run `make develop`. The interactive OpenAPI spec should open up in `http://localhost:8000/`.

To format and lint use the following respectively: `make format` and `make lint`.

## Dependencies / documentation

Here I outline a few dependencies/technologies used in this project, I recommend having a look into their documentation and use it for further reference:

- [DockerCompose](https://docs.docker.com/compose/): used for management of development containers only.
- [OpenAPI/Swagger](https://spec.openapis.org/oas/latest.html): Rest HTTP API specification format.
- [Fly.io](https://fly.io/docs/): Global application platform used to deploy the production container.

- [FastAPI](https://fastapi.tiangolo.com/): Python web framework;
- [Pipenv](https://pipenv.pypa.io/en/latest/): Python dependency management tool. Allows better control than the native PIP.
- [Pymongo](https://pymongo.readthedocs.io): the Python <> mongo driver.
- [pydantic](https://pydantic-docs.helpmanual.io/): Python dependency used to create and validate DTOs.
