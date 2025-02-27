"""
Service of YOLO.
YOLO is used to identify the border of any object in an image
"""

from configure.yolo_configure import yolo_model

SAVE_PATH = "src/sample"
CONF = 0.25


class Agent:
    def __init__(self):
        self.model = yolo_model

    def check_status(self):
        if self.model:
            return True
        else:
            return False

    # "path" can be a single file, or can be a directory
    # Or might be a list of string
    def process_image(self, path: str | list, info=None):

        results = self.model.predict(
            path, conf=CONF, save=True, project=SAVE_PATH, name="output"
        )

        # If you want to see the detailed information...
        if info:
            self.model.info()
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    print(
                        f"Type: {result.names[int(box.cls)]}",
                        f"Confidence: {box.conf}",
                        f"Coordinate: {box.xyxy[0].tolist()}",
                    )

        # Return results
        return results

    # Open the monitor
    def monitor(self):
        return self.model.predict(source="0", show=True)


# Export
yolo_service = Agent()
