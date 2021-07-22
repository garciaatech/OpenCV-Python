import cv2
import numpy as np

img = cv2.imread("Resources/souleater.jpg") #import image

kernel = np.ones((5,5),np.uint8) #matrix with (size) and values (type of object) #uint8 values range from 0 to 255

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #change image color

imgblur = cv2.GaussianBlur(imggray,(7,7),0) #blurs image

imgcanny = cv2.Canny(img,100,100) #find edges

imgdilation = cv2.dilate(imgcanny,kernel,iterations=1) #increase edge thiccness #iteration increases thiccness

imgeroded = cv2.erode(imgdilation,kernel,iterations=1) #make edge thinner

#print functions
cv2.imshow("Gray", imggray)
cv2.imshow("Blur", imgblur)
cv2.imshow("Canny", imgcanny)
cv2.imshow("Dilation", imgdilation)
cv2.imshow("Erode", imgeroded)

#delay
cv2.waitKey(0)