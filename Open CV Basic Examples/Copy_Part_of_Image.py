import cv2
import random

img = cv2.imread('Resources/people.jpg',-1)

tag = img[500:700,600:900]
img[100:300,650:950] = tag

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()