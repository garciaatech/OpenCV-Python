import cv2
import numpy as np

img = cv2.imread("Resources/souleater.jpg")
print(img.shape) #height, width, channels (BGR)

imgresize = cv2.resize(img,(300,200)) #width then height
print(imgresize.shape) #height, width, channels (BGR)

imgcropped = img[0:200,200:500] #height then width to keep

cv2.imshow("Image", img)
cv2.imshow("Resized", imgresize)
cv2.imshow("Cropped", imgcropped)

cv2.waitKey(0)