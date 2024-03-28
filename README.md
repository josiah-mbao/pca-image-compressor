# PCA Image Compression Project
## Overview

This project implements Principal Component Analysis (PCA) for compressing images. PCA is a dimensionality reduction technique that can be applied to images to reduce their size while preserving important information. In this project, we use PCA to compress images and evaluate the trade-offs between compression ratio and image quality.

## Key Takeaways and Lessons learned
1. To undertake this project, I had to learn the fundamentals of linear algebra. I improved my understanding on linear transformations, covariance matrices, eigenvalues and eigenvectors.
2. I brushed up my knowledge on statistical and machine learning concepts around covariance, feature extraction and dimension reduction.
3. I leveraged python libraries that made certain computations more efficient.
4. I learnt a bit about the basics of image processing.

## Requirements
Python 3.0 and above
NumPy
Scikit learn libraries

## Installation
Clone this repository:
```python
git clone https://github.com/your_username/pca-image-compression.git
```
Install dependencies:
```python
pip install numpy
pip install matplotlib
pip install scikit-learn
pip install scikit-image
```

## Usage
1. Place the images you want to compress in the images/ directory.
2. Run the compression script:
```python
python compress_images.py
```
3. Adjust the compression parameters as needed (e.g., number of principal components).
4. Compressed images will be saved in the output/ directory.

## Configuration
1. compress_images.py: Main script for compressing images.
2. utils.py: Contains helper functions for image processing and PCA.

## Parameters
1. num_components: Number of principal components to retain during compression. Higher ..* values preserve more image detail but result in larger file sizes.
2. input_dir: Directory containing input images.
3. output_dir: Directory to save compressed images.
4. image_format: Output image format (e.g., JPEG, PNG).

## Results
..* A comparison of an image before and after compression. It uses 2 principal components.
![Image compressed using dimension reduction aka. PCA](https://github.com/josiah-mbao/pca-image-compressor/blob/main/compressed%20output.png?raw=true)

## Acknowledgements
..* This project was developed for a university assignment for a Numerical Analysis course, instructed by Dr.J. Owino.

## License
..* This project is licensed under the MIT License - see the LICENSE file for details.

## Feedback
..* If you have any suggestions, bug reports, or feedback, please feel free to open an issue or contact Josiah Mbao.

