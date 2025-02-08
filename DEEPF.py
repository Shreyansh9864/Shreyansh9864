import deepface
import cv2
x= cv2.VideoCapture(0)
while True:
    ret,_=x.read()
    cv2.imshow("frame",_)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# After the loop release the cap object
x.release()