import joblib

# Load the trained model
try:
    model = joblib.load('trained_model.joblib')
except FileNotFoundError:
    raise Exception("Model file 'trained_model.joblib' not found. Please ensure the model is saved in the correct location.")