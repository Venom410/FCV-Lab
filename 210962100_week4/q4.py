# Import necessary libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

def kmeans(img, n_clusters, max_iters=100):
    # Get image dimensions
    h, w, _ = img.shape

    # Reshape image for clustering
    reshaped_img = img.reshape(h * w, -1)

    # Initialize cluster centers randomly
    np.random.seed(42)
    centers = reshaped_img[np.random.choice(h * w, n_clusters, replace=False)]

    # K-means iteration loop
    for _ in range(max_iters):
        # Assign each pixel to the nearest cluster center
        labels = np.argmin(np.linalg.norm(reshaped_img[:, np.newaxis] - centers, axis=-1), axis=-1)

        # Compute new cluster centers
        new_centers = np.array([reshaped_img[labels == k].mean(axis=0) for k in range(n_clusters)])

        # Check for convergence
        if np.all(centers == new_centers):
            break

        centers = new_centers

    # Assign pixels to final cluster centers and reshape to image dimensions
    clustered_img = centers[labels].reshape(h, w, -1).astype(np.uint8)

    return clustered_img

# Path to the input image
image_path = 'resources/Lenna.png'

# Load the input image using OpenCV
image = cv2.imread(image_path)

# Number of clusters for K-means
n_clusters = 3

# Apply K-means clustering to the image
clustered_image = kmeans(image, n_clusters)

# Create a 1x2 subplot grid for displaying images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(clustered_image)
plt.title(f'K-means Clustering ({n_clusters} clusters)')
plt.axis('off')

# Adjust layout for better visualization
plt.tight_layout()

# Display the plot containing the original and clustered images
plt.show()
