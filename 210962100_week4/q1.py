import cv2

# Path to the input image
img_path = 'resources/Lenna.png'

# Read the input image in grayscale mode
gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Apply different thresholding methods to the grayscale image
ret, thresh1 = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(gray_img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(gray_img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(gray_img, 120, 255, cv2.THRESH_TOZERO_INV)

# Display the original grayscale image
cv2.imshow('Original Grayscale', gray_img)

# Display the images obtained using different thresholding methods
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
