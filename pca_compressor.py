import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from skimage import io, transform

def compress_image(image_path, num_components=50, target_size=(100, 100)):
    # Loads the image
    image = io.imread(image_path)

    # Resizes the image, so all the images have the same num of features.
    image_resized = transform.resize(image, target_size, anti_aliasing=True)

    # Check if image is grayscale or color
    if len(image_resized.shape) == 3:  # Color image
        # Reshape image to a 2D array (flatten)
        original_shape = image_resized.shape
        image_resized = image_resized.reshape((-1, original_shape[2]))
    elif len(image_resized.shape) == 2:  # Grayscale image
        original_shape = image_resized.shape
        image_resized = image_resized.reshape((-1, 1))

    # Convert to float and normalize the data
    scaler = StandardScaler()
    normalized_image = scaler.fit_transform(image_resized.astype(np.float64))

    # Check for any invalid data
    if np.isnan(normalized_image).any() or np.isinf(normalized_image).any():
        print("Invalid data detected in the image.")
        return None

    # Apply PCA
    pca = PCA(n_components=num_components)
    compressed_image = pca.fit_transform(normalized_image)

    # Reconstruct the image
    reconstructed_image = pca.inverse_transform(compressed_image)

    # Reshape the image to its original shape
    reconstructed_image = reconstructed_image.reshape(original_shape)

    # Save the compressed image
    io.imsave(output_path, reconstructed_image.astype(np.uint8))

    return reconstructed_image

def plot_images(original_image, compressed_image):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(original_image)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(compressed_image)
    axes[1].set_title('Compressed Image')
    axes[1].axis('off')
    plt.show()

# this is the "if name=main()" section of the program. Or the script-executable part 

image_path = '/Users/josiah/Desktop/The Off Season Project/PCA Image Compression/images/manu_logo.png'  # Path to the image
output_path = '/Users/josiah/Desktop/The Off Season Project/PCA Image Compression/output/compressed_img.png'
num_components = 3  # Number of principal components
target_size = (100, 100)  # Target size for resizing the images
compressed_image = compress_image(image_path, num_components=num_components, target_size=target_size)

if compressed_image is not None:
    original_image = io.imread(image_path)
    plot_images(original_image, compressed_image)

