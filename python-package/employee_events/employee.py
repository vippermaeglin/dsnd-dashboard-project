# Import the QueryBase class
from sql_execution import QueryBase

# Import dependencies needed for SQL execution
import pandas as pd

# Define a subclass of QueryBase called Employee
class Employee(QueryBase):
    # Set the class attribute `name` to the string "employee"
    name = "employee"

    # Define a method called `names` that receives no arguments
    # This method should return a list of tuples from an SQL execution
    def names(self):
        # Query 3: Select the employee's full name and ID for all employees
        query = """
            SELECT CONCAT(first_name, ' ', last_name) AS full_name, employee_id 
            FROM employee
        """
        # Execute the query and return the results
        return self.run_query(query)

    # Define a method called `username` that receives an `id` argument
    # This method should return a list of tuples from an SQL execution
    def username(self, id):
        # Query 4: Select the full name of the employee with the specified ID
        query = f"""
            SELECT CONCAT(first_name, ' ', last_name) AS full_name
            FROM employee
            WHERE employee_id = {id}
        """
        # Execute the query and return the results
        return self.run_query(query)

    # Modify the `model_data` method to return a pandas dataframe
    def model_data(self, id):
        query = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        # Execute the query and return the results as a pandas dataframe
        return pd.read_sql(query, self.connection)
