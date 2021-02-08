import cv2

cap = cv2.VideoCapture(3)
cap.set(3, 640)
cap.set(4, 480)
while True:
    sucess, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(int(1000 / 30)) & 0xFF == ord("q"):
        break