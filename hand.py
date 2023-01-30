import cv2
from handTrackingModule import handDetector

cap = cv2.VideoCapture(0)

detector = handDetector()

while True:
    success , img = cap.read()
    img = detector.findHands(img)
    # lmLIst,bbox = detector.findPosition(img)
    
    cv2.imshow("image",img)
    cv2.waitKey(1)
    
    
    
                                      