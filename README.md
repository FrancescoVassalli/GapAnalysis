# Gap Analysis

A hackathon demo for finding gaps in coporate anit-phising processes.

## Getting Started

### **Clone the Repository**: Clone this repository to your local machine

```sh
git clone https://github.com/FrancescoVassalli/GapAnalysis.git
cd GapAnalysis
```

### **Open in VS Code**: Open the repository in Visual Studio Code

```sh
code .
```

## Setup

You can manually run a docker-compose environment or if you have Visual Studio Code with the Remote Containers extension you can use the [Dev Container](#dev-container) configuration.

1. Setup your `.env` - [see steps below](#environment-variables)
2. Have docker engine running on your system
3. In this directory `docker compose -f .devcontainer/docker-compose.yml up -d`
4. Go to `localhost:8000` to access the API

### Environment Variables

Create a `.env` file in the root directory of the project and add the necessary environment variables:
>[!TIP]
>
>You can copy [`.env.example`](./.env.example) and rename it to `.env` and fill in the necessary values

```env
OPENAI_API_KEY=<your_openai_api_key>
ENV=development
```

## Important API Endpoints

FastAPI has a built in Swagger UI that can be accessed at `localhost:8000/docs` or `localhost:8000/redoc`

TBD

## Dev Container

The [`.devcontainer`](.devcontainer) folder contains a development container configuration for the GapAnalysis project. The devcontainer is configured to provide a consistent development environment using Docker and Visual Studio Code.

### Prerequisites

1. [**Docker**](https://www.docker.com/): Ensure Docker is installed and running on your system.
2. [**Visual Studio Code**](https://code.visualstudio.com/): Install Visual Studio Code.
3. [**Remote - Containers Extension**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers): Install the Remote - Containers extension in Visual Studio Code.

### Open the Dev Container

- Press `F1` or `CMD/Ctrl` + `Shift` + `P` to open the command palette
  - Type and select `Remote-Containers: Reopen in Container`.

This will build and start the devcontainer defined in `.devcontainer/devcontainer.json`.

You can also click on the Remote Indicator in the **bottom-left status bar** to get a list of the most common commands. Remote Indicator status bar item: `><` to access this menu.

For more information, please see the [extension documentation](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) or the [devcontainers documentation](https://code.visualstudio.com/docs/devcontainers/containers).

### Running Services

This repo contains pre-configrued launch commands for the most common applications

In VS Code open the [Run and Debug](https://code.visualstudio.com/docs/editor/debugging) section or by pressing `F5`

Inside the Debug side bar you can Launch the services defined in [`.vscode/launch.json`](.vscode/launch.json)

- `Run Uvicorn`: Launches the FastAPI server

>Alternatively you can run `poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload` in the integrated terminal

### Setting up database

Run this command in the dev container to write the schema to the 

### Deployment to Docker Containers

This project includes Docker configurations for both the API and the UI. The `build` folder contains the necessary production Dockerfiles.

#### Building the API Docker Image

To build the Docker image for the API, navigate to the `build/api` directory and run the following command:

```sh
docker build -f build/api.Dockerfile -t gap-analysis-api .
```

#### Building the UI Docker Image

Before building the Docker image for the UI, you need to build the static files using npm. Navigate to the root directory of the project and run:

```sh
npm run build
```

After the build process is complete, navigate to the `build/ui` directory and run the following command to build the Docker image:

```sh
docker build -f build/ui.Dockerfile -t gap-analysis-ui .
```

### Deploying Docker Images

Once the Docker images are built, you can deploy them to any cloud provider that supports Docker, such as Digital Ocean, GCP, AWS, and more.

#### Example Deployment to Cloud

1. Push the Docker images to a container registry (e.g., Docker Hub, Digital Ocean Container Registry, Githube Container Registry, etc).
2. Run the Docker containers using the pulled images.

```sh
docker run -d --rm --name api -p 8000:8000 gap-analysis-api
docker run -d --rm --name ui -p 3000:3000 gap-analysis-ui
```

This will start the API on port `8000` and the UI on port `300`.

For more detailed instructions on deploying to other cloud providers, refer to their respective documentation.
