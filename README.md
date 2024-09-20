# Real Estate Manager CLI

## Description
This CLI application allows users to manage real estate agents, properties, and buyers using a simple command-line interface. It leverages SQLAlchemy for ORM and Alembic for database migrations.

## Features
- Add and view agents, properties, and buyers.
- Manage relationships between agents and properties.
- View properties based on agent and buyer details.

## Requirements
- Python 3.10
- Pipenv
- SQLAlchemy
- Alembic
- Tabulate

## Setup
1. Clone the repository.
2. Install dependencies: `pipenv install`
3. Initialize the database and apply migrations:
    ```bash
    pipenv run alembic upgrade head
    ```
4. Run the CLI:
    ```bash
    pipenv run python cli/main.py
    ```

## Usage
1. Follow the on-screen menu to add or view agents, properties, and buyers.
2. Use option '7' to exit the application.

