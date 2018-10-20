# -*- coding: utf-8 -*-
"""
Example 2-1

@author: Satoshi Murashige
"""

import cv2

# 指定したパスから画像を読み込む
img = cv2.imread('../images/color/Lenna.bmp')

# 画像の読み込みに失敗していたらエラーを吐いて終了
assert img is not None, 'Loading image is failed.'

# 'Example 2-1'という名前でウインドウを作り，画像を表示する
cv2.namedWindow('Example 2-1', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Example 2-1', img)

# キーが押されるまで待つ
cv2.waitKey(0)

# ウインドウExample 2-1を消す
cv2.destroyWindow('Example 2-1')

