import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640) #set width
cap.set(4, 480) #set height
cap.set(10, 100) #set brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break