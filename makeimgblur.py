import cv2
import numpy as np
from skimage.restoration import denoise_tv_chambolle
import os

# Get the absolute path to the image
# This makes the script runnable from any directory
image_path = os.path.join(os.path.dirname(__file__), 'ss', 'imges', 'b3.png')

# Read image in grayscale
# image = cv2.imread(r"C:\Users\mena.magdy\Desktop\python\ss\imges\b3.png", cv2.IMREAD_GRAYSCALE)
image = cv2.imread(r"C:\Users\mena.magdy\Desktop\python\ss\imges\blure2.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Error: Could not read the image. Please check the file path and integrity for: {image_path}")
else:
    # Denoise the image; the output is a float array in the range [0,1]
    denoised_float = denoise_tv_chambolle(image, weight=0.50)

    # Convert the float image back to an 8-bit unsigned integer for display
    # denoised_uint8 = (denoised_float * 50).astype(np.uint8)

    # Display the original and modified images
    cv2.imshow('Original Image', image)
    cv2.imshow('Denoised Image', denoised_float)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
