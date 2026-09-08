from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="video2.mp4",
    save=True,
    device=0
)