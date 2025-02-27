"""
Configuration of YOLO model
"""

from ultralytics import YOLO
import torch

from dotenv import load_dotenv
import os

# Load the pre-trained model
model = YOLO("yolo11l.pt")

# Modify your output path
save_dir = os.getenv("YOLO_OUT")

results = model.train(
    data="coco128.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    project=save_dir,
    name="qAI",
    exist_ok=True,
    patience=10,
)
