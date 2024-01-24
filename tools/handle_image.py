import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('../data/nike.png')

# Áp dụng lọc trung vị
filtered_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

# Hiển thị ảnh gốc và ảnh đã làm mờ
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()