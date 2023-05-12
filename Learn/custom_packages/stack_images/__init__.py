import cv2
import numpy as np


def stack_images(factor: float, images: list) -> None:
    def h_stack(image_list: list):
        return np.hstack(image_list)

    def v_stack(h_stacks: list):
        return np.vstack(h_stacks)

    length = len(images)
    assert length >= 0, 'No Images found in Input'

    for i in range(length):
        image = images[i]
        print(image.shape)
        height = int(image.shape[1] * factor)
        width = int(image.shape[0] * factor)
        image = cv2.resize(image, (height, width))

        if len(image) == 2:
            image = cv2.reshape(image, (height, width, 1))
        print(image.shape)

    if length == 1:
        h_stack = h_stack(images[0])
        cv2.imshow("Stack", h_stack)
        cv2.waitKey(0)

    elif length > 1:
        h_stack_list = []
        for i in range(length):
            h_stack_list.append(h_stack(images[i]))


        result = v_stack(h_stack_list)
        cv2.imshow("Stack", result)
        cv2.waitKey(0)

    else: pass

    return None
