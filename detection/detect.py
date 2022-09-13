import os
import time
import cv2
import numpy as np
from PIL import Image
from shapely.geometry import box as Box


def detect_obj(img_name):
    if img_name is None:
        img_name = r'resource/fake_img.png'  # demo

    print(img_name)

    if isinstance(img_name, str):
        img = cv2.imread(img_name)
        base_name = os.path.basename(img_name)
        base_path = os.path.dirname(img_name)
    else:
        img = cv2.cvtColor(np.asarray(img_name), cv2.COLOR_RGB2BGR)
        base_name = os.path.basename(os.path.join('./resource', 'fake_img_' + time.strftime('%Y%m%d_%H%M%S') + '.png'))
        base_path = r'./resource'

    r_info = []

    h, w = img.shape[:2]

    box = (w // 2 - w // 4, 10, w // 2 + w // 4, h - 10)

    # 转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 模糊和二值化
    # gray = cv2.blur(gray, (9, 9))
    gray = cv2.blur(gray, (5, 5))  # 模糊操作可能导致物体与边框颜色相似，从而导致二值化时物体被过滤掉
    # Image.fromarray(gray).show()
    # (_, thresh) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    (_, thresh) = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)  # 二值化的阈值根据色差设置
    # Image.fromarray(thresh).show()

    # 空隙填补
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 卷积核尺寸小一些，轮廓更明显（用于解决距离过近问题）
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # 去噪声
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    # 查找物体区域
    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print('物体区域：', cnts)
    # c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    print('-' * 40)
    # compute the rotated bounding box of the largest contour
    for i in range(len(cnts)):
        rect = cv2.minAreaRect(cnts[i])
        box_ = np.int0(cv2.boxPoints(rect))  # boxPoints返回顺序左上->右上->右下->左下
        # print(rect)
        # print(box_)
        # draw a bounding box arounded the detected barcode and display the image
        cv2.rectangle(img, box_[0], box_[2], (255, 255, 255), 1)

        # 根据两个矩形的左上和右下坐标判断是否相交
        M = (max(box[0], box_[0][0]), max(box[1], box_[0][1]))
        N = (min(box[2], box_[2][0]), min(box[3], box_[2][1]))
        print(box, box_)
        if Box(box[0], box[1], box[2], box[3]).intersects(
                Box(box_[0][0], box_[0][1], box_[2][0], box_[2][1])):  # (minx, miny, maxx, maxy, ccw=True)
            r_info.append((True, (box_[0][0], box_[0][1], box_[2][0], box_[2][1]), "物体在边界内"))
        # if box[0] < box_[0][0] and box[1] < box_[0][1] and box[2] > box_[2][0] and box[3] > box_[2][1]:
        #     r_info.append((True, box_, "物体在边界内"))
        #     # cv2.rectangle(img, box_[0], box_[2], (0, 255, 0), 1)
        # elif M[0] > N[0] or M[1] > N[1]:
        #     r_info = "该物体在边界外"
        #     # cv2.rectangle(img, box_[0], box_[2], (0, 255, 0), 1)
        # else:
        #     r_info = "物体与边界相交"
        #     # cv2.rectangle(img, box_[0], box_[2], (255, 0, 0), 1)
        # elif M[0] < N[0] and M[1] < N[1]:
        #     print("该物体与边界相交")
        #     cv2.rectangle(img, box_[0], box_[2], (255, 0, 0), 1)
        # else:
        #     print("物体在边界外")
        #     cv2.rectangle(img, box_[0], box_[2], (0, 255, 0), 1)

    # Image.fromarray(img).show()
    new_img_name = os.path.join(base_path, 'detect_' + base_name)
    cv2.imwrite(new_img_name, img)

    return tuple(r_info), new_img_name


if __name__ == '__main__':
    from generate import generate_random_image
    generate_random_image()
    x, y = detect_obj(generate_random_image())
    print(x)
