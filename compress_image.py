import numpy as np
import cv2
from utils import load_image, save_image, compress_image_with_pca

# TODO: I need to implement the helpers so that this works.

def main():
    # Parameters
    input_dir = "images/"
    output_dir = "output/"
    num_components = 50  # Number of principal components

    # Load input images
    image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]
    for file in image_files:
        image = load_image(input_dir + file)

        # Compress image using PCA
        compressed_image = compress_image_with_pca(image, num_components)

        # Save compressed image
        save_image(compressed_image, output_dir + file)

if __name__ == "__main__":
    main()

