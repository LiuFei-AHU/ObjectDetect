import random
import numpy as np
import cv2
from PIL import Image
import time
import os


def generate_random_image(save=False, save_path=None):
    img_shape = (256, 256, 3)
    fake_img = np.ones(shape=img_shape, dtype=np.uint8)
    h, w = fake_img.shape[:2]

    box = (w // 2 - w // 4, 10, w // 2 + w // 4, h - 10)
    print(box)

    # add random objects
    rec = (30, 50)
    COLORS = np.random.randint(0, 255, size=(3, 3), dtype='uint8')
    for i in range(3):
        hr = random.randint(0, h)
        wr = random.randint(0, w)
        print((wr - rec[0] // 2, hr - rec[1] // 2), (wr + rec[0] // 2, hr + rec[1] // 2))
        color = [int(c) for c in COLORS[i]]
        cv2.rectangle(fake_img, (wr - rec[0] // 2, hr - rec[1] // 2), (wr + rec[0] // 2, hr + rec[1] // 2), color, -1)

    # add box border
    print(box[0], box[1], box[2], box[3])
    cv2.rectangle(fake_img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 1)

    # save fake img
    if save:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, 'fake_img_' + time.strftime('%Y%m%d_%H%M%S') + '.png'), fake_img)

    return fake_img  # array 256x256

    # fake_img = Image.fromarray(fake_img)
    # fake_img.show()
