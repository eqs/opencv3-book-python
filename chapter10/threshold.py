# -*- coding: utf-8 -*-
"""
Example 10-3

@author: Satoshi Murashige
"""

import cv2
from matplotlib import pyplot as plt

# グレースケール画像として読みこむ
img = cv2.imread('../images/mono/girl.bmp', cv2.IMREAD_GRAYSCALE)

assert img is not None, 'Loading image is failed.'

# 127より明るい画素を255に，その他の画素を0にする
th_bin, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 大津の2値化
th_otsu, img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
# 適応的2値化 (Block Size: 11)
img_adap = cv2.adaptiveThreshold(img, 255, 
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                 cv2.THRESH_BINARY, 11, 2)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('src')
plt.subplot(2, 2, 2), plt.imshow(img_bin, cmap='gray'), plt.title(f'threshold (t={th_bin})')
plt.subplot(2, 2, 3), plt.imshow(img_otsu, cmap='gray'), plt.title(f'otsu (t={th_otsu})')
plt.subplot(2, 2, 4), plt.imshow(img_adap, cmap='gray'), plt.title('adaptive threshold')
plt.show()

