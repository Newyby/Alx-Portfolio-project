from flask import Flask, request, send_file  # Import necessary modules from Flask
from PIL import Image  # Import the Python Imaging Library (PIL)
from io import BytesIO  # Import BytesIO for handling image data

app = Flask(__name__)  # Create a Flask application instance

@app.route('/')  # Define a route for the homepage
def index():
    return app.send_static_file('index.html')  # Serve the static HTML file 'index.html' from the 'static' directory

@app.route('/compress', methods=['POST'])  # Define a route for compressing images via POST method
def compress():
    image = request.files['image']  # Access the uploaded image file from the request
    picture = Image.open(image)  # Open the image using PIL (Python Imaging Library)
    img_io = BytesIO()  # Create a BytesIO object to store the compressed image
    picture.save(img_io, 'JPEG', optimize=True, quality=30)  # Compress and save the image to the BytesIO object in JPEG format
    img_io.seek(0)  # Seek to the beginning of the BytesIO object
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')  # Send the compressed image file as a response

if __name__ == '__main__':
    app.run()  # Entry point to run the Flask application
