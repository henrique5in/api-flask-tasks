# Taskmanager

Task manager API using Flask.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip`:
  ```shell
  pip install -r requirements.txt
  ```

## Usage

1. Start the Flask server:
  ```shell
  python app.py
  ```
2. Access the API at `http://localhost:5000`.

## Endpoints

- **GET /api/tasks**: Get all tasks.
- **GET /api/tasks/{id}**: Get a specific task by ID.
- **POST /api/tasks**: Create a new task.
- **PUT /api/tasks/{id}**: Update an existing task.
- **DELETE /api/tasks/{id}**: Delete a task.