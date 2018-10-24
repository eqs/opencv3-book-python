# -*- coding: utf-8 -*-
"""
Example 10-1 

@author: Satoshi Murashige
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('../images/color/Lenna.bmp')

assert img_bgr is not None, 'Loading image is failed.'
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

img_rgb = np.float32(img_rgb) # 画像を8bit整数から32bit浮動小数点に変換する

img_r = img_rgb[:, :, 0] # 画像のR成分を取り出す
img_g = img_rgb[:, :, 1] # 画像のG成分を取り出す
img_b = img_rgb[:, :, 2] # 画像のB成分を取り出す

# 各チャネルの重み付き和でグレー画像を作る
img_gray = 0.299 * img_r + 0.587 * img_g + 0.144 * img_b

img_gray = np.uint8(img_gray) # 画像を8bit整数表現に戻す

plt.subplot(2, 2, 1), plt.imshow(img_r, cmap='gray'), plt.title('channel R')
plt.subplot(2, 2, 2), plt.imshow(img_g, cmap='gray'), plt.title('channel G')
plt.subplot(2, 2, 3), plt.imshow(img_b, cmap='gray'), plt.title('channel B')
plt.subplot(2, 2, 4), plt.imshow(img_gray, cmap='gray'), plt.title('Grayscale Image')
plt.show()
