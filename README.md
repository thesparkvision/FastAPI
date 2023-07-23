[![CI](https://github.com/thesparkvision/FastAPI/actions/workflows/build_and_run.yaml/badge.svg)](https://github.com/thesparkvision/FastAPI/actions/workflows/build_and_run.yaml)

## Intro

This repository is to practice FastAPI code while learning it

## Live App Link

https://fastapi-learning.onrender.com/

## Setup

**Python Version**: 3.11.1

- Create Virtual env
    
    ```shell
    python3 -m venv venv
    ```

- Install Packages

    ```shell
    pip install -r requirements.txt
    ```

- Add these environment variables in .env file or in shell

    ```
    export MONGO_URI=mongodb://172.17.0.2:27017
    export PYTHONPATH=$PYTHONPATH:$PWD
    export APP_HOST=0.0.0.0
    export APP_PORT=8000
    ```

- Install MongoDB or use MongoDB Docker Image (https://hub.docker.com/_/mongo)

## Run the app directly in local environment inside src folder

```shell
python3 main.py
```

## Local Docker Container Setup

If you prefer to use docker container,
or need to debug the build for some reason,
you can follow these chain of commands:

- Build the Docker Image

    ```shell
    docker build . -t fastapi-learning:v1 -f deploy/Dockerfile
    ```

- Create and Run Docker container

    ```shell
    docker run -d --net=host fastapi-learning:v1
    ```

## Run Lint

```shell
bash scripts/lint.sh
```
