import cv2
print("Package Imported")

img = cv2.imread("Resources/souleater.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)