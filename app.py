from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('second.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        return "No image provided", 400

    image = request.files['image']
    
    try:
        # Open the image using PIL
        picture = Image.open(image)

        # Compress the image
        compressed_img_io = BytesIO()
        picture.save(compressed_img_io, 'JPEG', optimize=True, quality=30)
        compressed_img_io.seek(0)

        return send_file(compressed_img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')
    except Exception as e:
        return f"Error compressing image: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)

