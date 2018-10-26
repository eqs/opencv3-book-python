# -*- coding: utf-8 -*-
"""
Example original filter

@author: Satoshi Murashige
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_noise(img, p=0.05):
    """ 画像にノイズを重畳する関数 """

    # 画素数
    npixels = img.size
    random_indices = np.random.permutation(npixels)
    # ノイズが重畳される画素のインデックス
    salt_idx   = random_indices[:int(npixels*p/2.0)]
    pepper_idx = random_indices[int(npixels*p/2.0):int(npixels*p)]
    # 画像をフラットにした配列を取得
    img_flat = img.flatten()
    img_flat[salt_idx] = 255
    img_flat[pepper_idx] = 0

    return img_flat.reshape(img.shape)

#' グレースケール画像として読みこむ
img = cv2.imread('../images/mono/BRIDGE.bmp', cv2.IMREAD_GRAYSCALE)

assert img is not None, 'Loading image is failed.'

# ノイズの割合
p = 0.15
# ノイズを重畳する
img_noise = apply_noise(img, p)
# 2種類のフィルタによってノイズを除去する
img_median = cv2.medianBlur(img, 5)
img_blur = cv2.blur(img, (5, 5))

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('src')
plt.subplot(2, 2, 2), plt.imshow(img_noise, cmap='gray'), plt.title(f'noise (p={p})')
plt.subplot(2, 2, 3), plt.imshow(img_median, cmap='gray'), plt.title('dst (median)')
plt.subplot(2, 2, 4), plt.imshow(img_blur, cmap='gray'), plt.title('dst (blur)')
plt.tight_layout()
# plt.savefig('median.pdf')
plt.show()



