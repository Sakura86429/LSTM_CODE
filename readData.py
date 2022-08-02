import cv2  #OpenCV包
import numpy as np

# 首先确定原图片的基本信息：数据格式，行数列数，通道数
# rows=5120#图像的行数
# cols=4096#图像的列数

cols=5120#图像的列数 width
rows=4096#图像的行数  height
channels =1# 图像的通道数，灰度图为1

# 利用numpy的fromfile函数读取raw文件，并指定数据格式
# img=np.fromfile(r'F:\h_1_3_00_2_4_0_0_5_30_01_0_00.raw', dtype='uint8')
# img=np.fromfile(r'F:\h_1_3_00_2_4_0_0_5_30_01_0_00.raw', dtype='uint16')
img=np.fromfile('F:\h_1_3_00_2_4_0_0_5_30_01_0_00.raw', dtype='uint16')
# 利用numpy中array的reshape函数将读取到的数据进行重新排列。
print(img.shape)
img=img.reshape(rows, cols)

# 展示图像
# cv2.imshow('Infared image-640*512-8bit',img)
# 如果是uint16的数据请先转成uint8。不然的话，显示会出现问题。
# cv2.waitKey()
# cv2.destroyAllWindows()
cv2.imwrite('F:\\' + 'h_1_3_00_2_4_0_0_5_30_01_0_00.png', img)
print('ok')

