from fasthtml.common import *
import matplotlib.pyplot as plt

# Import QueryBase, Employee, Team from employee_events
from employee_events import QueryBase, Employee, Team

# Import the load_model function from the utils.py file
from utils import load_model

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
)

from combined_components import FormGroup, CombinedComponent

# Subclass of `Dropdown` for report selection
class ReportDropdown(Dropdown):
    def build_component(self, model, *args, **kwargs):
        # Set the label attribute to the model's name
        self.label = model.name
        return super().build_component(model, *args, **kwargs)
    
    def component_data(self, model, *args, **kwargs):
        # Use the model to fetch user-type names and IDs
        return model.names()

# Subclass of `BaseComponent` for the header
class Header(BaseComponent):
    def build_component(self, model, *args, **kwargs):
        # Return an H1 element with the model's name attribute
        return H1(model.name)

# Subclass of `MatplotlibViz` for a line chart
class LineChart(MatplotlibViz):
    def visualization(self, model, asset_id, *args, **kwargs):
        # Fetch event counts from the model
        df = model.event_counts(asset_id)
        df = df.fillna(0).set_index('event_date').sort_index()
        df = df.cumsum()
        df.columns = ['Positive', 'Negative']

        fig, ax = plt.subplots()
        df.plot(ax=ax)

        # Style the plot
        self.set_axis_styling(ax)
        ax.set_title('Cumulative Event Counts')
        ax.set_xlabel('Date')
        ax.set_ylabel('Events')
        return fig

# Subclass of `MatplotlibViz` for a bar chart
class BarChart(MatplotlibViz):
    predictor = load_model()

    def visualization(self, model, asset_id, *args, **kwargs):
        # Fetch data for predictions
        data = model.model_data(asset_id)
        probas = self.predictor.predict_proba(data)
        probas = probas[:, 1]  # Second column

        # Determine prediction value
        if model.name == 'team':
            pred = probas.mean()  # Mean for teams
        else:
            pred = probas[0]  # First value for individuals

        # Create the bar chart
        fig, ax = plt.subplots()
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)

        self.set_axis_styling(ax)
        return fig

# Subclass of `CombinedComponent` for visualizations
class Visualizations(CombinedComponent):
    children = [LineChart(), BarChart()]
    outer_div_type = Div(cls='grid')

# Subclass of `DataTable` for notes
class NotesTable(DataTable):
    def component_data(self, model, entity_id, *args, **kwargs):
        # Fetch notes for the entity
        return model.notes(entity_id)

# Subclass of `FormGroup` for dashboard filters
class DashboardFilters(FormGroup):
    id = "top-filters"
    action = "/update_data"
    method = "POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
        ),
        ReportDropdown(
            id="selector",
            name="user-selection"
        )
    ]

# Subclass of `CombinedComponent` for the full report
class Report(CombinedComponent):
    children = [
        Header(),
        DashboardFilters(),
        Visualizations(),
        NotesTable()
    ]

# Initialize a FastHTML app
app = FastHTML()

# Initialize the `Report` class
report = Report()

# Define routes
@app.get('/')
def root():
    # Call the report with no ID and a QueryBase instance
    return report(None, QueryBase())

@app.get('/employee/{id:str}')
def employee_report(id):
    # Call the report for a specific employee
    return report(id, Employee())

@app.get('/team/{id:str}')
def team_report(id):
    # Call the report for a specific team
    return report(id, Team())

# Keep the provided code for updating dropdowns and handling form submissions unchanged

serve()
