# -*- coding: utf-8 -*-
"""
Example original filter

@author: Satoshi Murashige
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# グレースケール画像として読みこむ
img = cv2.imread('../images/mono/Airplane.bmp', cv2.IMREAD_GRAYSCALE)

assert img is not None, 'Loading image is failed.'

# Embossフィルタ
emboss = np.array([[1, 0, 0], 
                   [0, 0, 0], 
                   [0, 0,-1]])
# Gaussianフィルタ
gauss = cv2.getGaussianKernel(9, -1)
# Gaborフィルタ
gabor = cv2.getGaborKernel(ksize=(9, 9), sigma=5, theta=np.pi/2, lambd=50, gamma=3)
# フィルタを適用する
img_emb = cv2.filter2D(img, ddepth=-1, kernel=emboss)
img_gauss = cv2.filter2D(img, ddepth=-1, kernel=gauss)
img_gabor = cv2.filter2D(img, ddepth=-1, kernel=gabor)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('src')
plt.subplot(2, 2, 2), plt.imshow(img_emb, cmap='gray'), plt.title('Emboss')
plt.subplot(2, 2, 3), plt.imshow(img_gauss, cmap='gray'), plt.title('Gaussian')
plt.subplot(2, 2, 4), plt.imshow(img_gabor, cmap='gray'), plt.title('Gabor')
plt.tight_layout()
#plt.savefig('original.pdf')
plt.show()



