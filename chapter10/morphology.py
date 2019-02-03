# -*- coding: utf-8 -*-
"""
Example for morphology transformation

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

# 真っ黒な画像を作る
img = np.zeros((200, 200))

# 画像の上に "ABC" という文字列を書く
cv2.putText(img, 'ABC', (25, 100), cv2.FONT_HERSHEY_PLAIN, 
            5.0, (255, 255, 255), 5)

# ノイズを乗せる
img_noise = apply_noise(np.zeros((200, 200)), p=0.05)
img = cv2.bitwise_xor(img, img_noise)

# 構造化要素を作る
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

# 各種モルフォロジー変換をかける
img_dilate = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
img_erode  = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
img_open   = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_close  = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(2, 3, 1), plt.imshow(img       , cmap='gray'), plt.title('src')
plt.subplot(2, 3, 2), plt.imshow(kernel    , cmap='gray'), plt.title('Structuring Element')
plt.subplot(2, 3, 3), plt.imshow(img_dilate, cmap='gray'), plt.title('Dilation')
plt.subplot(2, 3, 4), plt.imshow(img_erode , cmap='gray'), plt.title('Erosion')
plt.subplot(2, 3, 5), plt.imshow(img_open  , cmap='gray'), plt.title('Opening')
plt.subplot(2, 3, 6), plt.imshow(img_close , cmap='gray'), plt.title('Closing')

plt.tight_layout()
# plt.savefig('derivative.pdf')
plt.show()



