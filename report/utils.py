import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# Set to the absolute path for the root of this project directory
project_root = Path(__file__).resolve().parent

# Using the `project_root` variable
# Create a `model_path` variable
# Pointing to the file `model.pkl` inside the assets directory
model_path = project_root / 'assets' / 'model.pkl'

def load_model():
    # Load the model from the specified path
    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model
