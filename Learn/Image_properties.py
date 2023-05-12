import cv2
import numpy as np

img = cv2.imread("Resources/Screenshot 2023-05-12 at 7.32.20 AM.png")
kernel = np.ones((11, 11), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgBlur = cv2.GaussianBlur(imgGray, (11, 11), 0)  # defining a kernel/filter size in the second attribute
imgCanny = cv2.Canny(img, 200, 200)  # Edge Display
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# dilation is basically increasing the thickness of edges and number of iterations controls this thickness with
# reference to the kernel size
imgEroded = cv2.erode(imgDilation, kernel, iterations=4)

# cv2.imshow("Original", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
# cv2.imshow("HSV", imgHsv)
# cv2.imshow("Dilation", imgDilation)
# cv2.imshow("Eroded", imgEroded)
cv2.waitKey(0)

# cv2.imwrite("looksLikeAnNFT.jpg", imgDilation)