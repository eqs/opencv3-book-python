# -*- coding: utf-8 -*-
"""
Example for derivative

@author: Satoshi Murashige
"""

import cv2
from matplotlib import pyplot as plt

# グレースケール画像として読みこむ
img = cv2.imread('../images/mono/girl.bmp', cv2.IMREAD_GRAYSCALE)

assert img is not None, 'Loading image is failed.'

# Sobelフィルタを水平方向にかける
sobel_x = cv2.Sobel(img, ddepth=-1, dx=1, dy=0)
# Sobelフィルタを垂直方向にかける
sobel_y = cv2.Sobel(img, ddepth=-1, dx=0, dy=1)
# Laplacianフィルタをかける
img_lap = cv2.Laplacian(img, ddepth=-1, ksize=3)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('src')
plt.subplot(2, 2, 2), plt.imshow(sobel_x, cmap='gray'), plt.title('sobel x')
plt.subplot(2, 2, 3), plt.imshow(sobel_y, cmap='gray'), plt.title('sobel y')
plt.subplot(2, 2, 4), plt.imshow(img_lap, cmap='gray'), plt.title('laplacian')
plt.tight_layout()
# plt.savefig('derivative.pdf')
plt.show()



