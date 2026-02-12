from ultralytics import YOLO

class PhoneDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def phone_present(self, frame):
        results = self.model(frame, verbose=False)
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                if self.model.names[cls] == "cell phone":
                    return True
        return False
