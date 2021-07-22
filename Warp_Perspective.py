import cv2
import numpy as np

img = cv2.imread("Resources/souleater.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) #set points of object to warp to
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #set detail about above points
matrix = cv2.getPerspectiveTransform(pts1,pts2) #create matrix of points

imgoutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Image Warp",imgoutput)

cv2.waitKey(0)