import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sakam\wp3097243-nancy-jewel-mcdonie-wallpapers.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
gradient_mask = cv2.Laplacian(blurred, cv2.CV_64F)


sharpened = np.uint8(gray - 0.5 * gradient_mask)  


cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
