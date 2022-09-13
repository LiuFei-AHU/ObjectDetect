#目标轮廓提取算法1,


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


#图片二值化
def get_binary_img(img):
    # gray img to bin image
    bin_img = np.zeros(shape=(img.shape), dtype=np.uint8)
    h = img.shape[0]
    w = img.shape[1]
    for i in range(h):
        for j in range(w):
            bin_img[i][j] = 255 if img[i][j] > 127 else 0
    return bin_img

#图片轮廓提取
def get_contour(bin_img):
    # get contour
    contour_img = np.zeros(shape=(bin_img.shape), dtype=np.uint8)
    contour_img += 255
    h = bin_img.shape[0]
    w = bin_img.shape[1]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if (bin_img[i][j] == 0):
                contour_img[i][j] = 0
                sum = 0
                sum += bin_img[i - 1][j + 1]
                sum += bin_img[i][j + 1]
                sum += bin_img[i + 1][j + 1]
                sum += bin_img[i - 1][j]
                sum += bin_img[i + 1][j]
                sum += bin_img[i - 1][j - 1]
                sum += bin_img[i][j - 1]
                sum += bin_img[i + 1][j - 1]
                if sum == 0:
                    contour_img[i][j] = 255

    return contour_img



#读入彩色照片
img_name = "1.jpg"
img = cv2.imread(img_name)


#彩色图片灰度化
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#灰度图片二值化
bin_img = get_binary_img(gray_img)

#图片轮廓提取
contour_img = get_contour(bin_img)

output = Image.fromarray(contour_img)
output.show()



