# -*- coding: utf-8 -*-
"""
Example 2-3

@author: Satoshi Murashige
"""

import cv2

# 画像表示用のウインドウを作る
cv2.namedWindow('Example 2-3', cv2.WINDOW_AUTOSIZE)

# カメラから映像を読み込むVideoCaptureを作る
cap = cv2.VideoCapture(0)

# ファイルから映像を読み込むVideoCaptureを作る
# cap = cv2.VideoCapture('video_file.avi') 

# キャプチャを開くのに失敗したら終了
assert cap.isOpened(), 'Cannot open the video.'

while True:
    
    # キャプチャからフレームをひとつ読み込む
    ok, frame = cap.read()
    
    # フレームが読み込めなかったなら終了
    if not ok:
        break
    
    # 読み込んだフレームを表示
    cv2.imshow('Example 2-3', frame)
    
    # キーの入力を33ミリ秒待つ
    key = cv2.waitKey(33)
    
    # キーが押されたなら終了する
    if key >= 0:
        break

# 後始末処理
cap.release()
cv2.destroyAllWindows()

