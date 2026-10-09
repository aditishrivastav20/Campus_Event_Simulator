# Campus Event Registration Workflow Simulator

## About the Project
The Campus Event Registration Workflow Simulator is a
Python-based application designed to manage campus events
and participant registrations.

It allows users to create events, register participants,
view registrations, cancel registrations, and export
registration data to a CSV file.

## Features
- Create and view campus events
- Register participants for events
- Validate participant IDs, emails, and mobile numbers
- Prevent duplicate registrations
- Check event capacity before registration
- Cancel participant registrations
- View registration records
- Export registration data to CSV
- Store data in JSON files
- Maintain application logs
- Automated validation testing

## Technologies Used
- Python
- JSON
- CSV
- Regular Expressions
- Logging
- Unittest

## Project Structure

    Campus_Event_Simulator/
    ├── main.py
    ├── event_service.py
    ├── validators.py
    ├── storage.py
    ├── logger_config.py
    ├── data/
    ├── logs/
    └── tests/
        └── test_validators.py

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the application:

       python main.py

## How to Run Tests

Run the following command from the project root:

    python -m unittest discover -s tests -v

## Learning Outcomes
- Python functions and modules
- Input validation
- File handling using JSON and CSV
- Exception handling
- Application logging
- Automated testing

## Project Status
Core functionality and validation tests implemented.