from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from pca_compressor import compress_image
from skimage import io

app = Flask(__name__)

# Directories for images
UPLOAD_FOLDER = 'images/'
OUTPUT_FOLDER = 'output/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            
            # Compress the image and generate the plot
            compressed_image = compress_image(filename, num_components=3, target_size=(100, 100))
            
            if compressed_image is not None:
                original_image = io.imread(filename)
                plot_images(original_image, compressed_image)
                
                return render_template('index.html', compressed_image='compressed_img.png', plot='plot.png')

    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Compression settings (can be dynamic later)
        compressed_image = compress_image(image_path, num_components=3, target_size=(100, 100))
        compressed_image_path = os.path.join(app.config['OUTPUT_FOLDER'], 'compressed_' + file.filename)
        io.imsave(compressed_image_path, compressed_image)

        return redirect(url_for('download_image', filename='compressed_' + file.filename))

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/output/<filename>')
def serve_output_file(filename):
    return send_from_directory('output', filename)

if __name__ == "__main__":
    app.run(debug=True)
