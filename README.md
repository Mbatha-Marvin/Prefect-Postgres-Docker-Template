# Prefect Postgres Docker/Podman Compose

---

This project shows how you can dockerize a simple Prefect project. The project serves the flows using the serve utility in prefect. You can serve multiple flows and pipelines using the serve utilty in prefect. 

***Note there are various ways to structure your prefect projects to best fit your needs***

### Project Structure

---

```bash
├── orchestrator
│   ├── prefect_app
│   │   ├── app
│   │   │   ├── core
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── pipelines
│   │   │   │   ├── hello_world
│   │   │   │   │   ├── deployment.py
│   │   │   │   │   ├── flows
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── main_flow.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── tasks
│   │   │   │   │   │   ├── hello.py
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── utils
│   │   │   │   │       ├── date.py
│   │   │   │   │       └── __init__.py
│   │   │   │   └── __init__.py
│   │   │   └── utils
│   │   │       └── __init__.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── pyproject.toml
│   ├── README.md
│   └── requirements.txt
├── compose.yaml
├── Dockerfile
├── example.env
└── README.md
```

##### Project Overview

---

***orchestrator/prefect_app*** - project base directory. I used poetry to initialize this project. 

***orchestrator/prefect_app/main.py*** - the entry point for the prefect deployment. If this file is not present in your project the prefect_deployments service will likely fail. If you decide to move it ensure you adjust your imports accordingly.

***orchestrator/prefect_app/app*** -  prefect flows are defined here .You can structure this module to fit your standards and preference. If you do restructure it, make the imports in your project reflect your project structure. 

***orchestrator/prefect_app/app/core*** - stores project-wide configuration files

***orchestrator/prefect_app/app/utils*** - stores project-wide utility files

***orchestrator/prefect_app/app/pipelines*** - stores pipelines and the supporting files and modules.

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

##### Steps:

1. Clone the repo
   
   ```bash
   git clone 
   cd 
   ```

2. Rename the example.env file to .env

3. Check if the ports used in the project are available. if they are not available adjust the ports set in the .env file to fit your environment

4. Build and run the project
   
   ```bash
   podman-compose up --build -d
   ```

5.  If you used the defaults in the .env file, go to your browser and go to:
   
   ```bash
   http://localhost:4200
   ```

        You will be able to see the hello_world_flow and hello_world_deployment.
