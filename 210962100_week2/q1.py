import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the grayscale image
img = cv2.imread('C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject1/210962100_week2/resources/Lenna.png', 0)

# Apply contrast stretching using the specified mapping
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
stretched_img = cv2.LUT(img, table)

# Apply histogram equalization to the contrast-stretched image
equ = cv2.equalizeHist(stretched_img)

# Create a stacked image with original, stretched, and equalized versions side by side
res = np.hstack((img, stretched_img, equ))

# Display the stacked image using OpenCV
cv2.imshow('Images', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot histograms of the original, stretched, and equalized images
plt.subplot(131)  # First subplot for original image histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Original Image Histogram')

plt.subplot(132)  # Second subplot for stretched image histogram
plt.hist(stretched_img.ravel(), 256, [0, 256])
plt.title('Stretched Image Histogram')

plt.subplot(133)  # Third subplot for equalized image histogram
plt.hist(equ.ravel(), 256, [0, 256])
plt.title('Equalized Image Histogram')

plt.show()  # Display the combined histogram plots
