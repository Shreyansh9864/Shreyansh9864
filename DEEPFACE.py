# #
# #
# from ultralytics import YOLO
# #
# model = YOLO("yolov5n.pt")
# #   # pass any model type
# #
# # # results = model(source=0,show=True,conf=0.4,save=True)
# result=model.predict(source="0",show=True)
# print(result)
# # # from ultralytics import YOLO
# # #
# # # # Load a model
# # # model = YOLO("yolov8n.yaml")  # build a new model from YAML
# # # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
# # # model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights
# # #
# # # # Train the model
# # # results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
#
#
import cv2 as cv
from ultralytics import YOLO
cap=cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while True:

     ret,img = cv.imread()
     cv.imshow(img)
     model = YOLO("YOLO8n.pt")
     class_name = ["Person","dog","Tooth-brush","cat","bag","Helmet","fish","food","tv","animal","mouse","keyboard","laptop","monitor","Trash-can","anime","cartoon","tooth-brush"]
    

     if cv.waitKey(2) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()


