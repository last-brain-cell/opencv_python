import cv2
import numpy as np
# from custom_packages.stack_images import stack_images

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def empty(do_nothing):
    pass


# Objective -> Color Detection

# Making TrackBars(Sliders) in a Window
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 9, 179, empty)  # Name, TargetWindow
cv2.createTrackbar("Hue Max", "TrackBars", 15, 179, empty)  # Name, TargetWindow
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)  # Name, TargetWindow
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)  # Name, TargetWindow
cv2.createTrackbar("Val Min", "TrackBars", 126, 255, empty)  # Name, TargetWindow
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)  # Name, TargetWindow

# img = cv2.imread("Resources/markers.jpeg")
# imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

try:
    while True:
        success, img = cap.read()
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        hue_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        val_max = cv2.getTrackbarPos("Val Max", "TrackBars")

        # print(f"{hue_min} {hue_max} {sat_min} {sat_max} {val_min} {val_max}")

        # mask filter
        lower = np.array([hue_min, sat_min, val_min])
        upper = np.array([hue_max, sat_max, val_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        # cv2.imshow("Original", img)
        # cv2.imshow("HSV", imgHSV)
        # cv2.imshow("Mask", mask)
        # cv2.imshow("Result", imgResult)
        h_stack = np.hstack((img, imgResult))

        cv2.imshow("Color Detection", h_stack)
        cv2.waitKey(1)
        # stack_images(0.3, [[img, imgResult]])

except:
    print("Program Ended")
