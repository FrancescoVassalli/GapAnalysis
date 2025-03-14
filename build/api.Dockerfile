# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11-slim-bookworm

RUN apt-get update && apt-get -y install \
  libpq-dev gcc

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY pyproject.toml poetry.toml alembic.ini ./

# Install any needed packages specified in requirements.txt
RUN pip install poetry
RUN poetry install --no-root --no-interaction --no-ansi --only main

COPY *.py ./
COPY migrations ./migrations

# Make port 8000 available to the world outside this container
EXPOSE 8000

# By default launch the API
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
