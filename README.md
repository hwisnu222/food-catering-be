# Food Catering BE

This is the backend-end for the Food Catering website, built using Django Graphql(graphene-django).

## Prerequisites

- Docker
- Docker Compose
- Python3.9 - optional for local development
- Git

## Installation

Before running the project, first clone the repository using the following command:

```bash
git clone https://github.com/hwisnu222/food-catering-be.git
cd food-catering-be
```

## Running the Project

After installing the necessary packages, the next step is to run the project. To do this, use the following command:

```bash
docker compose up -d
```

Then, access the application in your browser at [http://localhost:8000/graphql](http://localhost:8000/graphl).

## Run the Frontend Project

To run the frontend project alongside the backend, you also need to clone and run the frontend repository. Use the following commands:

```bash
git clone https://github.com/hwisnu222/food-catering-fe.git
cd food-catering-fe
docker compose up -d
```

This will start the frontend project, and both front-end and back-end will run simultaneously.
