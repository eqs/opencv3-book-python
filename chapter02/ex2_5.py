# -*- coding: utf-8 -*-
"""
Example 2-5

@author: Satoshi Murashige
"""

import cv2
from matplotlib import pyplot as plt

# グレースケール画像を読み込む
img_src = cv2.imread('../images/mono/BRIDGE.bmp')
assert img_src is not None, 'Loading image is failed.'

# 画像をぼかす処理をかける
img_dst = cv2.blur(img_src, (9, 9))

plt.subplot(1, 2, 1), plt.imshow(img_src), plt.title('src image')
plt.subplot(1, 2, 2), plt.imshow(img_dst), plt.title('dst image')
plt.show()

