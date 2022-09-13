import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_name = r"../moon.jpg"
img = cv2.imread(img_name)
print(img.shape)  # picture size

# assume a fixed box
h, w, _ = img.shape
box = (w//2-w//4, 10, w//2+w//4, h-10)
print(box)

cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 1)
# Image.fromarray(img_box).show()
base_path = os.path.basename(img_name)
cv2.imwrite('with_box_' + base_path, img)

# Image.fromarray(np.asarray(img)).save('with_box_' + base_path)