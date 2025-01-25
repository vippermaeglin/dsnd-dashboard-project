
# Software Engineering for Data Scientists 

This repository contains starter code for the **Software Engineering for Data Scientists** final project. Please reference your course materials for documentation on this repository's structure and important files. Happy coding!

### Repository Structure
```
├── README.md
├── assets
│   ├── model.pkl
│   └── report.css
├── env
├── python-package
│   ├── employee_events
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   ├── employee_events.db
│   │   ├── query_base.py
│   │   ├── sql_execution.py
│   │   └── team.py
│   ├── requirements.txt
│   ├── setup.py
├── report
│   ├── base_components
│   │   ├── __init__.py
│   │   ├── base_component.py
│   │   ├── data_table.py
│   │   ├── dropdown.py
│   │   ├── matplotlib_viz.py
│   │   └── radio.py
│   ├── combined_components
│   │   ├── __init__.py
│   │   ├── combined_component.py
│   │   └── form_group.py
│   ├── dashboard.py
│   └── utils.py
├── requirements.txt
├── start
├── tests
    └── test_employee_events.py
```

### employee_events.db

```mermaid
Diagram

  employee {
    INTEGER employee_id PK
    TEXT first_name
    TEXT last_name
    INTEGER team_id
    
  }

  employee_events {
    TEXT event_date
    INTEGER employee_id FK
    INTEGER team_id FK
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER employee_id PK
    INTEGER team_id PK
    TEXT note
    TEXT note_date PK
  }

  team {
    INTEGER team_id PK
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }

  team ||--o{ employee_events : "team_id"
  employee ||--o{ employee_events : "employee_id"
  notes }o--o{ employee_events : ""
```

## Run Instructions
### Simple SQL models validation
In order to validate Employee/Team models, just execute the `test.py` class under `/python/employee_events`
### Build & Install
Go into python folder:
> cd python

Build the package:
> python setup.py sdist bdist_wheel

Install the package in editable mode:
> pip install -e .

Verify the installation:
> pip show employee_events

### Run the FastAPI
Go back to root folder:
> cd ..

Run the application:
> uvicorn report.dashboard:app --host 0.0.0.0 --port 8000 --reload

Open API in browser:
> http://localhost:8000

### Validate Endpoints
Show dashboard for an employee:
> http://localhost:8000/employee/2

Show dashboard for a team:
> http://localhost:8000/team/2
 
Show dropdown values with all employees:
> http://localhost:8000/update_dropdown?profile_type=Employee

Show dropdown values with all teams:
> http://localhost:8000/update_dropdown?profile_type=Team

