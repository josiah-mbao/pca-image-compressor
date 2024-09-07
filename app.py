from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from pca_compressor import compress_image
from skimage import io
from werkzeug.utils import secure_filename
import secrets

app = Flask(__name__)

# Set a secret key for session management and security features
app.secret_key = secrets.token_hex(16)

# Directories for images
UPLOAD_FOLDER = 'images/'
OUTPUT_FOLDER = 'output/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['image']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Compress the image using PCA
        compressed_image_filename = compress_image(filepath, num_components=3)
        
        # Ensure the file was created successfully
        if not compressed_image_filename:
            flash('Compression failed')
            return redirect(request.url)
        
        # Render template with compressed image
        return render_template('index.html', 
                               filename=filename, 
                               compressed_image=compressed_image_filename)
    else:
        flash('Invalid file type')
        return redirect(request.url)



@app.route('/download/<filename>')
def download_image(filename):
     # Add the prefix 'compressed_' to the filename
    compressed_filename = 'compressed_' + filename
    return send_from_directory(app.config['OUTPUT_FOLDER'], compressed_filename)

@app.route('/output/<filename>')
def serve_output_file(filename):
    return send_from_directory('output', filename)

if __name__ == "__main__":
    app.run(debug=True)
