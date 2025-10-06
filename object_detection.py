import cv2
from ultralytics import YOLO

# تحميل YOLOv8
model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame, verbose=False)
    objects = []  # قائمة من tuples: (label, width, height)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])

            if conf > 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                width = x2 - x1
                height = y2 - y1

                objects.append((label, width, height))

                # رسم bounding box دايمًا
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame, objects