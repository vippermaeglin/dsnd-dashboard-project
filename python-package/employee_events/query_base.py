# Import any dependencies needed to execute SQL queries
import pandas as pd
from sqlite3 import connect

# Define a class called QueryBase that has no parent class
class QueryBase:
    # Create a class attribute called `name` and set it to an empty string
    name = ""

    # Define a `names` method that receives no arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):
        # QUERY 1
        # Write an SQL query that groups by `event_date` and sums the number
        # of positive and negative events
        query = f"""
            SELECT 
                event_date,
                SUM(positive_events) AS positive_events,
                SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date
        """
        # Open a connection, execute the query, and return a dataframe
        with connect("employee_events.db") as conn:
            return pd.read_sql(query, conn)

    # Define a `notes` method that receives an `id` argument
    # This method should return a pandas dataframe
    def notes(self, id):
        # QUERY 2
        # Write an SQL query that returns `note_date` and `note`
        # from the `notes` table for the relevant `id`
        query = f"""
            SELECT 
                note_date,
                note
            FROM notes
            JOIN {self.name} USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        # Open a connection, execute the query, and return a dataframe
        with connect("employee_events.db") as conn:
            return pd.read_sql(query, conn)
