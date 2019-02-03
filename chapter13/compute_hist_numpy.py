# -*- coding: utf-8 -*-
"""
Numpyでヒストグラムを計算する

@author: Satoshi Murashige
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 画像を読みこむ
img = cv2.imread('../images/color/Earth.bmp')

assert img is not None, 'Loading image is failed.'

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(311), plt.hist(img[:, :, 0].ravel(), bins=256, range=[0, 256]), plt.title('R channel')
plt.subplot(312), plt.hist(img[:, :, 1].ravel(), bins=256, range=[0, 256]), plt.title('G channel')
plt.subplot(313), plt.hist(img[:, :, 2].ravel(), bins=256, range=[0, 256]), plt.title('B channel')
plt.tight_layout()
plt.savefig('compute_hist_numpy.pdf')
plt.show()

