# Prefect Postgres Docker/Podman Compose

---

This project shows how you can dockerize a simple Prefect project. The project serves the flows using the serve utility in prefect. You can serve multiple flows and pipelines using the serve utilty in prefect.

***Note there are various ways to structure your prefect projects to best fit your needs***

## Project Structure

---

```bash
.
├── orchestrator
│   ├── prefect_app
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── __init__.py
│   │   ├── deployments
│   │   │   └── hello_world.py
│   │   ├── flows
│   │   │   ├── hello_world.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── pipelines
│   │   │   └── __init__.py
│   │   ├── tasks
│   │   │   ├── hello.py
│   │   │   └── __init__.py
│   │   └── utils
│   │       ├── date.py
│   │       └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── README.md
│   └── requirements.txt
├── compose.yaml
├── Dockerfile
├── example.env
└── README.md
```

### Project Overview

---

***orchestrator/prefect_app*** - project base directory. I used poetry to initialize this project.

***orchestrator/prefect_app/main.py*** - the entry point for the prefect deployment. If this file is not present in your project the prefect_deployments service will likely fail. If you decide to move it ensure you adjust your imports accordingly.

***orchestrator/prefect_app/flows*** -  prefect flows and subflows are defined here .

***orchestrator/prefect_app/tasks*** - prefect tasks for your various flows are defined here .

***orchestrator/prefect_app/core*** - stores project-wide configuration files

***orchestrator/prefect_app/utils*** - stores project-wide utility files

***orchestrator/prefect_app/pipelines*** - for complex pipelines, you can create pipelines in this folder for a more organization

**The compose file defines 3 services:**

1. prefect_database -  stores Prefect metadata

2. prefect_server

3. prefect_deployments - creates a long running process using your defined flow.

### Installation

---

#### Prerequisites

To successfully run this project you need to have the following installed and running:

- Docker / Podman

- Docker compose / Podman compose

#### How to run

---

I have podman installed incase you have docker replace 'podman' with 'docker' in all the commands.

##### Steps

1. Clone the repo
   
   ```bash
   git clone https://github.com/Mbatha-Marvin/Prefect-Postgres-Docker-Template.git
   cd Prefect-Postgres-Docker-Template
   ```

2. Rename the example.env file to .env

3. Check if the ports used in the project are available. if they are not available adjust the ports set in the .env file to fit your environment

4. Build and run the project
   
   ```bash
   podman-compose up --build -d
   ```

5. If you used the defaults in the .env file, go to your browser and go to:
   
   ```bash
   http://localhost:4200
   ```

        You will be able to see the hello_world_flow and hello_world_deployment.
