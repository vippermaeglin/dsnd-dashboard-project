# Import the QueryBase class
from query_base import QueryBase

# Import dependencies for SQL execution
import pandas as pd

# Create a subclass of QueryBase called `Team`
class Team(QueryBase):
    
    # Set the class attribute `name` to the string "team"
    name = "team"

    def names(self):
        """Retrieve all team names and their IDs."""
        sql_query = f"""
            SELECT team_name, team_id
            FROM {self.name}
        """
        return self.query(sql_query)

    def username(self, id):
        """Retrieve the name of a team based on its ID."""
        sql_query = f"""
            SELECT team_name
            FROM {self.name}
            WHERE team_id = {id}
        """
        return self.query(sql_query)

    def model_data(self, id):
        """Retrieve aggregated positive and negative event data for a team."""
        sql_query = f"""
            SELECT positive_events, negative_events 
            FROM (
                SELECT employee_id,
                       SUM(positive_events) AS positive_events,
                       SUM(negative_events) AS negative_events
                FROM {self.name}
                JOIN employee_events
                    USING({self.name}_id)
                WHERE {self.name}.{self.name}_id = {id}
                GROUP BY employee_id
            )
        """
        return self.pandas_query(sql_query)
