import cv2
import numpy as np


# Define custom Gaussian blur function
def custom_gaussian_blur(image, kernel_size, sigma):
    height, width = image.shape[:2]
    half_kernel_size = kernel_size // 2

    blurred_image = np.zeros_like(image, dtype=np.float32)

    for y in range(height):
        for x in range(width):
            pixel_sum = 0
            weight_sum = 0

            for ky in range(-half_kernel_size, half_kernel_size + 1):
                for kx in range(-half_kernel_size, half_kernel_size + 1):
                    if 0 <= y + ky < height and 0 <= x + kx < width:
                        weight = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(kx ** 2 + ky ** 2) / (2 * sigma ** 2))
                        pixel_sum += image[y + ky, x + kx] * weight
                        weight_sum += weight

            blurred_image[y, x] = pixel_sum / weight_sum

    blurred_image = blurred_image.astype(np.uint8)
    return blurred_image


# Load the image
image_path = 'C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject(210962100)/210962100_week3/resources/Lenna.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply custom Gaussian blur
custom_gaussian_filtered = custom_gaussian_blur(image, kernel_size=5, sigma=1.0)  # Kernel size: 5x5, Sigma: 1.0

# Apply box filter
box_filtered = cv2.boxFilter(image, -1, (3, 3))  # Kernel size: 3x3

# Display the original image and custom Gaussian filtered image
cv2.imshow('Original Image', image)
cv2.imshow('Custom Gaussian Filtered', custom_gaussian_filtered)
cv2.imshow('Box filtered',box_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
