## Project Overview

Apache Airflow DAG for orchestrating the Spotify ETL pipeline.
Schedules and monitors daily runs of extract, validate, transform, and load tasks.

## Architecture diagram

Airflow DAG
- Task 1: extract    → Read from S3
- Task 2: validate   → check data types
- Task 3: transform  → clean data
- Task 4: load       → save CSV

## Tech stack

- Language: Python 3.11
- Database: PostgreSQL
- Orchestration: Apache Airflow
- Storage: AWS S3
- Containerization: Docker
- CI/CD: GitHub Actions

## How to run

1.Clone repo
2.cp .env.example (.env) and put credentials
3.docker-compose up
4.python etl_spotify.py
5.python load_to_postgres.py
