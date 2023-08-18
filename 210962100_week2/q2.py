import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the source and reference images
source_image = cv2.imread('C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject(210962100)/210962100_week2/resources/Lenna.png', 0)
reference_image = cv2.imread('C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject(210962100)/210962100_week2/resources/Lenna1.png', 0)

# Calculate histograms of the source and reference images
source_hist = cv2.calcHist([source_image], [0], None, [256], [0, 256])
reference_hist = cv2.calcHist([reference_image], [0], None, [256], [0, 256])

# Display the histograms before histogram specification
plt.subplot(221)
plt.plot(source_hist, color='b')
plt.title('Source Image Histogram')
plt.subplot(222)
plt.plot(reference_hist, color='b')
plt.title('Reference Image Histogram')

# Calculate CDFs of the source and reference histograms
source_cdf = np.cumsum(source_hist)
reference_cdf = np.cumsum(reference_hist)

# Perform histogram specification
lut = np.interp(source_cdf, reference_cdf, np.arange(256))

# Apply the mapping to the source image
specified_image = cv2.LUT(source_image, lut)

# Display the specified image
cv2.imshow('Specified Image', specified_image/255)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculate the histogram of the specified image using numpy
specified_hist, _ = np.histogram(specified_image, bins=256, range=[0, 256])

# Display the histogram after histogram specification
plt.subplot(223)
plt.plot(specified_hist, color='b')
plt.title('Specified Image Histogram')

plt.show()  # Display the histograms
