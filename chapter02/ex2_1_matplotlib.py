# -*- coding: utf-8 -*-
"""
Example 2-1 with Matplotlib

@author: Satoshi Murashige
"""

import cv2
from matplotlib import pyplot as plt

img_bgr = cv2.imread('../images/color/Lenna.bmp')

assert img_bgr is not None, 'Loading image is failed.'
assert len(img_bgr.shape) == 3, 'Loaded image is not color'

# 画像をBGRからRGBに変換する
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Matplotlibによって画像を表示する
plt.subplot(1, 2, 1), plt.imshow(img_bgr), plt.title('BGR image')
plt.subplot(1, 2, 2), plt.imshow(img_rgb), plt.title('RGB image')
plt.show()

