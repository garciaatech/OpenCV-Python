import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #size and channels
# print(img)
# img[:] = 0,255,0 #change whole image color
# img[200:300,100:300] = 255,0,0 #change certain place in image

#                      width        height                #
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),6) #create line
# cv2.rectangle(img,(0,0),(250,350),(0,255,0),cv2.FILLED)
cv2.rectangle(img,(0,0),(250,350),(0,255,0),4) #create rectangle
cv2.circle(img,(400,50),30,(255,0,0),5) #create circle
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_ITALIC,1,(60,50,100),1) #create text

cv2.imshow("Image",img)

cv2.waitKey(0)