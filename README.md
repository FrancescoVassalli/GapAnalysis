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
