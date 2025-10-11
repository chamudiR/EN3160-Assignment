import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('the_berry_farms_sunflower_field.jpg', cv2.IMREAD_GRAYSCALE)

sigmas = np.linspace(2, 10, 5)  # Example scales
blob_list = []

for sigma in sigmas:
    blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=sigma)
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    # Find maxima and threshold (add your own logic)
    # e.g., maximum filtering, thresholding, non-max suppression
    # Store (x, y, sigma) if maxima detected

# Draw circles on input image
for blob in blob_list:
    x, y, r = blob
    cv2.circle(img, (x, y), int(r), (255, 0, 0), 2)  # blue circles

plt.imshow(img, cmap='gray')
plt.show()

