import cv2
import time

# cap = cv2.VideoCapture("Resources/20190421_082807.mp4")
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # id for width = 3
cap.set(4, 480)  # id for height = 4
# cap.set  # id for brightness = 10

start = 0
end = 0

while True:
    success, img = cap.read()
    start = time.time()

    font = cv2.FONT_HERSHEY_SIMPLEX
    frame_time = (start-end)
    end = time.time()

    fps = str(int(round(1 / frame_time, 0)))
    cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("Weird Video", imgHSV)
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
