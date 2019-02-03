# -*- coding: utf-8 -*-
"""
Histogramを計算する

@author: Satoshi Murashige
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 画像を読みこむ
img = cv2.imread('../images/color/Earth.bmp')

assert img is not None, 'Loading image is failed.'

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 各色チャネルについてヒストグラムを計算
hist_r = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
hist_b = cv2.calcHist([img], [2], None, [256], [0, 256])

# ヒストグラム同士を比較する
print('R-G: {0}'.format(cv2.compareHist(hist_r, hist_g, cv2.HISTCMP_BHATTACHARYYA)))
print('R-B: {0}'.format(cv2.compareHist(hist_r, hist_b, cv2.HISTCMP_BHATTACHARYYA)))
print('G-B: {0}'.format(cv2.compareHist(hist_g, hist_b, cv2.HISTCMP_BHATTACHARYYA)))

plt.subplot(121)
plt.imshow(img)
plt.title('src')

plt.subplot(122)
plt.plot(hist_r, 'r-', label='R channel')
plt.plot(hist_g, 'g-', label='G channel')
plt.plot(hist_b, 'b-', label='B channel')
plt.title('histograms')
plt.xlabel('Brightness')
plt.ylabel('Frequency')
plt.legend(loc='best')

plt.tight_layout()
# plt.savefig('compute_hist.pdf')
plt.show()

