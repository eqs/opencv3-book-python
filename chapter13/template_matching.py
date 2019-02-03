# -*- coding: utf-8 -*-
"""
Template Matching

@author: Satoshi Murashige
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 画像を読みこむ
img = cv2.imread('../images/mono/LENNA.bmp', cv2.IMREAD_GRAYSCALE)

assert img is not None, 'Loading image is failed.'

# テンプレート画像をひっこぬく
img_template = img[100:100+100, 95:95+90]

# テンプレートマッチングを実行 (正規化二乗差分マッチング)
result = cv2.matchTemplate(img, img_template, cv2.TM_SQDIFF_NORMED)

# 距離マップの最小値と場所 (テンプレートの左上座標) を探す
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

p = (min_loc[1] + img_template.shape[1], 
     min_loc[0] + img_template.shape[0]) # 右下の座標

# 最小値がみつかった場所に枠を描く
img_out = cv2.rectangle(img.copy(), min_loc, p, (0, 255, 0), 2)

plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('src')
plt.subplot(222), plt.imshow(img_template, cmap='gray'), plt.title('template')
plt.subplot(223), plt.imshow(result), plt.title('distance map')
plt.colorbar()
plt.subplot(224), plt.imshow(img_out, cmap='gray'), plt.title('result')

plt.tight_layout()
# plt.savefig('template_matching.pdf')
plt.show()

