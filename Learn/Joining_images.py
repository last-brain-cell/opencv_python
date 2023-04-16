import cv2
import numpy as np


def imgStack(factor, images: list):
    for nested_list in images:
        for image in nested_list:
            cv2.resize(image, (int(image.shape[1] * factor), int(image.shape[0] * factor)))

    hstack1 = images[0][0]
    hstack2 = images[1][0]
    for i in range(1, len(images[0])):
        hstack1 = np.hstack((hstack1, images[0][i]))
        hstack2 = np.hstack((hstack2, images[1][i]))
    stack = np.vstack((hstack1, hstack2))

    cv2.imshow("Stacked Images", stack)


img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgBlur = cv2.GaussianBlur(imgGray, (11, 11), 0)
imgCanny = cv2.Canny(img, 500, 500)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=4)
imgEroded = cv2.erode(imgDilation, kernel, iterations=4)


imgStack(0.5, [[img, imgHsv], [imgHsv, img]])
imgStack(0.5, [[imgGray, imgDilation], [imgCanny, imgEroded]])
cv2.waitKey(0)