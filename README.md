# JFS - Jira Fucking Sucks

This is an interactive, menu-driven Python script that leverages the JIRA REST API.

## Setup

1. Clone this repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Copy `config.yaml.example` to `config.yaml` and fill in your JIRA API details.

## Usage

Run the script with `python -m src.menu`

## Adding New Menu Options

To add a new menu option:

1. Add a new function in `jira_api.py` that performs the desired action.
2. Add a new option in `menu.py` that calls this function.

## Running Tests

Run tests with `pytest tests/`