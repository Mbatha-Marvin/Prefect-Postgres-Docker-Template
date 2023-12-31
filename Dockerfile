FROM python:3.11.7-slim

WORKDIR /app

# Install dependencies

COPY ./orchestrator/requirements.txt ./

RUN pip install -r requirements.txt

# Run your app
COPY ./orchestrator/ ./