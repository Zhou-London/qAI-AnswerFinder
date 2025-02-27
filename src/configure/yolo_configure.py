"""
Configuratino of YOLO model.
If you didn't train your model, please do it before configuration.
"""

from ultralytics import YOLO

from dotenv import load_dotenv
import os


# Make sure you run the program from qAI/
# Otherwise the path could not be found
load_dotenv()
MODEL_PATH = os.getenv("YOLO_PATH")


class model:

    def __init__(self):
        self.model = None
        self.load()

    # Load the file
    def load(self):
        try:
            self.model = YOLO(MODEL_PATH)
        except Exception as e:
            print("Failed to load the YOLO model")


yolo_model = model().model
