"""
Configuration of YOLO model
"""

from ultralytics import YOLO
import torch

from dotenv import load_dotenv
import os

load_dotenv()

# Load the pre-trained model
model = YOLO("/Users/zhou/repo/qAI/src/configure/yolo_output/text/weights/last.pt")

# Modify your output path
save_dir = os.getenv("YOLO_OUT")

results = model.train(
    data="/Users/zhou/repo/qAI/src/configure/yolo_dataset/text_dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    device="mps",
    project=save_dir,
    name="text",
    exist_ok=True,
    patience=10,
    resume=True,
)

print("Saved to", save_dir)
