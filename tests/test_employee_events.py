import pytest
from pathlib import Path

# Using pathlib, create a project_root variable set to the absolute path
# for the root of this project
project_root = Path(__file__).resolve().parent

# Apply the pytest fixture decorator to a `db_path` function
@pytest.fixture
def db_path():
    # Using the `project_root` variable
    # Return a pathlib object for the `employee_events.db` file
    return project_root / "employee_events.db"

# Define a function called `test_db_exists`
# This function should receive an argument with the same name as the function
# that creates the "fixture" for the database's filepath
def test_db_exists(db_path):
    # Using the pathlib `.is_file` method
    # Assert that the SQLite database file exists
    # at the location passed to the test_db_exists function
    assert db_path.is_file(), f"Database file does not exist at {db_path}"

# Define a test function called `test_employee_table_exists`
# This function should receive the `table_names` fixture as an argument
def test_employee_table_exists(table_names):
    # Assert that the string 'employee' is in the table_names list
    assert "employee" in table_names, "Employee table does not exist in the database"

# Define a test function called `test_team_table_exists`
# This function should receive the `table_names` fixture as an argument
def test_team_table_exists(table_names):
    # Assert that the string 'team' is in the table_names list
    assert "team" in table_names, "Team table does not exist in the database"

# Define a test function called `test_employee_events_table_exists`
# This function should receive the `table_names` fixture as an argument
def test_employee_events_table_exists(table_names):
    # Assert that the string 'employee_events' is in the table_names list
    assert "employee_events" in table_names, "Employee events table does not exist in the database"
