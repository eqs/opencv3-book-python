# -*- coding: utf-8 -*-
"""
Example 2-11

@author: Satoshi Murashige
"""

import cv2

cv2.namedWindow('Example 2-11', cv2.WINDOW_AUTOSIZE)

cap = cv2.VideoCapture(0)
assert cap.isOpened(), 'Cannot open the video.'

# キャプチャからサイズの情報をとってくる
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 15.0

# 動画保存用のVideoWriterを作る
writer = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'MJPG'), fps, (width, height))

# 100フレームだけ保存する
for k in range(100):
    
    ok, frame = cap.read()
    
    if not ok:
        break
    
    cv2.imshow('Example 2-11', frame)
    writer.write(frame)
    
    key = cv2.waitKey(33)
    if key >= 0:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

