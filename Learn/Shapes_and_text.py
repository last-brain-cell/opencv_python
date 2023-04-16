import cv2
import numpy as np
import random

lambo = cv2.imread("Resources/lambo.jpeg")
print(lambo.shape)


# Resizing an Image
def resize(image, factor):
    print(image.shape)
    print(f"Changing Size of Image and number of pixels {factor}X.")
    img_resize = cv2.resize(image, (int(image.shape[1] / factor), int(image.shape[0] / factor)))

    print(img_resize.shape)
    cv2.imshow("Image", image)
    cv2.imshow("Resized Image", img_resize)
    cv2.waitKey(0)


# Cropping an Image
def crop(image, height: tuple, width: tuple):
    img_cropped = img[height[0]:height[1], width[0]:width[1]]
    cv2.imshow("Cropped Image", img_cropped)
    cv2.waitKey(0)
    print("Cropped Image")


# Drawing Shapes on Images
def shapes():
    img = np.zeros((512, 512, 3), np.uint8)
    img[:] = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # shapes
    cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 3)  # drawing a line
    cv2.rectangle(img, (200,200), (400, 344), (0, 255, 0), cv2.FILLED)  # drawing a rectangle
    cv2.circle(img, (100, 200), 40, (0, 0, 255), cv2.FILLED)  # drawing a rectangle

    # Text
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, " OpenCV ", (300, 400), font, 1, (0, 169, 0), 2)

    cv2.imshow("Blank", img)
    cv2.waitKey(0)


resize(lambo, eval(input("Enter factor: ")))
# crop(lambo, (300, 569), (69, 420))
# shapes()