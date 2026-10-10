API Data Collector

A Python project that collects data from a public REST API, processes JSON responses, and saves the results to a local file.

Features
HTTP GET requests using requests
HTTP status code validation
JSON response processing
Local JSON file persistence
Exception handling for network and file errors
Technologies
Python
Requests
JSON
pathlib
Requirements
Python 3.10 or newer
pip
Installation

Clone the repository:

git clone https://github.com/benosantos/api-data-collector.git
cd api-data-collector


Create and activate a virtual environment.

On Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1


Install the dependencies:

python -m pip install -r requirements.txt

Usage

Run the application:

python main.py


The program retrieves a task from JSONPlaceholder, displays its information in the terminal, and saves the response to tarefa.json.

Learning Objectives

This project was created to practice Python fundamentals, REST API integration, HTTP error handling, JSON processing, and file management.

Future Improvements
Add automated tests with pytest
Collect multiple records from the API
Improve input and response validation
Add structured logging
Author

GitHub: @benosantos