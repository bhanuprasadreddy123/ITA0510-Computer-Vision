import cv2
import numpy as np
cap = cv2.VideoCapture("E:/Computer Vision/computer vision input and output/6videoinput.mp4")
if (cap.isOpened()== False):
          Print("Error opening video file")
while(cap.isOpened()):
          ret, frame = cap.read()
          if ret == True:
              cv2.imshow('Frame', frame)
              if cv2.waitKey(250) & 0xFF == ord('q'):
                         break
          else:
                 break
cap.release()
cv2.destroyAllWindows()
