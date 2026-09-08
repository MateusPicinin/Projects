from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model("cidade.jpg", save=True)
print("Resultado Concluido!")