# Use an official Python runtime as a parent image
FROM python:3.11-bookworm

SHELL ["/bin/bash", "-c"]

# Define a build argument to control Node.js installation
ARG INSTALL_NODE=false

# Conditionally install Node.js if INSTALL_NODE is set to true
RUN if [ "$INSTALL_NODE" = "true" ]; then \
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && \
  . ~/.nvm/nvm.sh && nvm install 22; \
  else \
  echo "Skipping Node.js installation"; \
  fi

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY pyproject.toml ./

# Install any needed packages specified in requirements.txt
RUN pip install poetry
RUN poetry install --no-root --all-extras --with dev

# Make port 8000 available to the world outside this container
EXPOSE 8000

# By default launch the API
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
