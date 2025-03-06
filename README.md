
# Software Engineering for Data Scientists 

This repository contains starter code for the **Software Engineering for Data Scientists** final project. Please reference your course materials for documentation on this repository's structure and important files. Happy coding!

### Business Requirements
* You are a data scientist for a manufacturing company.
* Your company's upper management have expressed concern about losing their best employees to competitors.
* To address this concern, the data team you're assigned to has done the following work:
  * A data entry form was deployed to managers that allows them to record an employee's positive and negative performance events
  * A database called employee_events has been created that stores the inputs from the manager form
  * A data scientist on your team has developed a machine learning model using data from this new database that predicts the likelihood of an employee being recruited by another company
* You have been assigned the following responsibility: Build a dashboard that allows managers to monitor an employee's performance and their predicted risk of recruitment. This dashboard must fulfill the following business requirements:
  * The dashboard visualizes the productivity of a single employee or a team of employees
  * The dashboard displays an employee's likelihood of recruitment, or a team of employees' average likelihood of recruitment
 
### Technical Requirements
* Your company has more than one data science team, and each team works with different databases. To ensure business-critical datasets are tested and accessible to all data teams, each data team is required to publish Python APIs for the databases they work with. This means for the new database:
  * You must develop SQL queries that generate business-critical datasets.
  * You must develop a Python package that allows users to generate critical datasets without needing to write the queries themselves.
* Your team has published previous dashboards using FastHTML. You are tasked with using your team's existing FastHTML codebase to develop your dashboard. This means:
  * Your must familiarize yourself with the code your team has written and the repository structure used for storing the code.
  * You must use your knowledge of Object Oriented Programming to extend and customize pre-built Python classes.
 
### Stack
* Python
* Pandas
* SQLite
* FastHTML
* MatPlotLib
* Scikit-Learn

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

```

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

### Python Requirements
From the root directory:
> pip install -r requirements.txt

### Build & Install
Go into python folder:
> cd python

Build the package:
> python setup.py sdist bdist_wheel

Install the package in editable mode:
> pip install -e .

Verify the installation:
> pip show employee_events
 
![image](https://github.com/user-attachments/assets/cf8f6ec9-e467-4227-b25e-343fab9435e1)

### Run the FastAPI
Go back to root folder:
> cd ..

Run the application:
> python -m uvicorn report.dashboard:app --host 0.0.0.0 --port 8000 --reload

Open API in browser:
> http://localhost:8000
<img width="814" alt="image" src="https://github.com/user-attachments/assets/de0f7091-d4e9-41f5-8cd5-32018e356929" />

### Validate Endpoints
Show dashboard for an employee:
> http://localhost:8000/employee/2

Show dashboard for a team:
> http://localhost:8000/team/2
 
Show dropdown values with all employees:
> http://localhost:8000/update_dropdown?profile_type=Employee

Show dropdown values with all teams:
> http://localhost:8000/update_dropdown?profile_type=Team

