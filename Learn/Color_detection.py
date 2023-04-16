import cv2
import numpy as np


def empty(do_nothing):
    pass


# Objective -> Color Detection

# Making TrackBars(Sliders) in a Window
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)  # Name, TargetWindow
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)  # Name, TargetWindow
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)  # Name, TargetWindow
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)  # Name, TargetWindow
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)  # Name, TargetWindow
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)  # Name, TargetWindow

while True:
    img = cv2.imread("Resources/markers.jpeg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # os.system("cls" if os.name == "nt" else "clear")
    # print(f"{hue_min} {hue_max} {sat_min} {sat_max} {val_min} {val_max}")

    # mask filter
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)
    # stack_im  ages(0.3, [[img, imgHSV], [mask, imgResult]])