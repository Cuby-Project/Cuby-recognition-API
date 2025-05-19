import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'color_model.pkl')

# Load once at import
model = joblib.load(MODEL_PATH)

def classify_hsv_pixel(hsv_pixel):
    hsv_array = np.array(hsv_pixel).reshape(1, -1)
    prediction = model.predict(hsv_array)
    return prediction[0]
