from ultralytics import YOLO
# from deepface import DeepFace
MODEL = YOLO("Yolov8n.pt")

result = MODEL.predict(source="3",show=True,stream=False,save=True)
print(result)
# deepface = DeepFace.analyze(result)
# print(deepface)
# print(result)s