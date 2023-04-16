import cv2
import time

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # id for width = 3
cap.set(4, 480)  # id for height = 4
# cap.set(9, 1)  # id for brightness = 10

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
    # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("Video", imgHSV)
    cv2.imshow("Video", imgHSV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
