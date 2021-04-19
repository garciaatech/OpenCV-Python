import cv2

img = cv2.imread('Resources/shapes.jpg')
imgre = cv2.resize(img,(0,0),fx=2,fy=2)
imgrot = cv2.rotate(img,cv2.cv2.ROTATE_180)

cv2.imwrite('new_img.jpg',img)

cv2.imshow("image",img)
cv2.imshow("image resize",imgre)
cv2.imshow("image rotate",imgrot)
cv2.waitKey(0)
cv2.destroyAllWindows()