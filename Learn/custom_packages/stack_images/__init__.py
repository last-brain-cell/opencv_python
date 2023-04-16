import cv2
import numpy as np
from math import sqrt


def stack_images(factor: float, images: list):
    # resize
    count = 0
    for row in images:
        for image in row:
            height = int(image.shape[1] * factor)
            width = int(image.shape[0] * factor)
            channels = image.shape[-1]
            print(channels)
            cv2.resize(image, (height, width))

            if channels != 3:
                image.reshape(height, width, 1)

            count += 1

    # height = images[0][0].shape[1]
    # width = images[0][0].shape[0]
    # hstack = np.zeros((height, width))
    # hstack.reshape((height, width, 1))
    # vstack = hstack
    # in_one_row = int(sqrt(count))
    # cols = len(images)
    #
    # for i in range(cols):
    #     for j in range(in_one_row):
    #         hstack = np.hstack((hstack, images[i][j]))
    #
    #     vstack = np.vstack((vstack, hstack))
    #
    # cv2.imshow("Result", vstack)
    cv2.waitKey(1)
