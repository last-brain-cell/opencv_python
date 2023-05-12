import cv2
from custom_packages.stack_images import stack_images

img = cv2.imread("Resources/shapes.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

# cv2.imshow("Image", img)
# cv2.imshow("GrayScale", imgGray)
# cv2.imshow("Blur", imgBlur)
# print(img.shape)
# print(imgGray.shape)

stack_images(1.2, [imgGray, imgBlur])

