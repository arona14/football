# Football Management API

A FastAPI-based REST API for managing football leagues, teams, and players.

## Features

- Manage football leagues
- Track teams and their information
- Maintain player records
- RESTful API endpoints
- SQLite database for data persistence

## Tech Stack

- Python 3.12
- FastAPI
- SQLModel (SQLAlchemy + Pydantic)
- Uvicorn
- Poetry for dependency management

## Prerequisites

- Python 3.12 or higher
- Poetry package manager

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd football
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## Running the Application

Start the development server:
```bash
uvicorn football.main:app --reload
```

The API will be available at `http://localhost:8000`

## Running Tests

```bash
poetry run pytest
```
## API Documentation

Once the server is running, you can access:
- Swagger UI documentation at `http://localhost:8000/docs`
- ReDoc documentation at `http://localhost:8000/redoc`

## Project Structure

```
football/
├── football/
│   ├── leagues/     # League-related models and routes
│   ├── teams/       # Team-related models and routes
│   ├── players/     # Player-related models and routes
│   ├── main.py      # FastAPI application entry point
│   └── database.py  # Database configuration
├── tests/           # Test files
├── pyproject.toml   # Project dependencies and metadata
└── poetry.lock      # Lock file for dependencies
```

## Author

- Arona14 (sowarona14@gmail.com)
