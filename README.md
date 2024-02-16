[Alx Portfolio project github](https://github.com/Newyby/Alx-Portfolio-project.git)

[Image compression website landing page](https://newyby.github.io/Alx-test-project/)

[Image compression website Demo](http://127.0.0.1:5000)     

[Image compression website github](https://github.com/Newyby/Compression-of-image.git)











IMAGE COMPRESSION USING PYTHON AND INSTALLING NECESSARY DEPENDANCY
Steps to design a Python framework for an image compression algorithm:

Choose a compression algorithm: The first step is to select an image compression algorithm that you want to implement. Some popular algorithms are JPEG, PNG, and GIF.

Install the necessary libraries: Once you have chosen your compression algorithm, you need to install the necessary libraries to implement it.We are using JPEG compression then we install pillow library.

Create a class for the compression algorithm: Next, we create a class for compression algorithm. This class should contain methods for compressing and decompressing images, also we included methods for setting compression parameters.

Create a function to read images: Create a function to read images from disk or from memory.

Create a function to write compressed images: Create a function to write compressed images to disk or memory.

Create a function to compress images: Create a function that takes an image as input and returns the compressed image.

Create a function to decompress images: Create a function that takes a compressed image as input and returns the decompressed image.

Test your framework: Finally,we test for the framework by compressing and decompressing various types of images and comparing the results with the original images.

Image Compression Web
This is a simple web application built using Flask framework that allows users to compress images. The application accepts an image file from the user, compresses it using JPEG optimization with a quality setting of 30, and returns the compressed image for download.

Requirements
Python 3.x                                                                              Flask
PIL (Python Imaging Library)
Installation                                                                            Clone the repository or download the source code files.
Install the required dependencies using pip:

pip install flask pillow                                                                Usage
Open a terminal or command prompt and navigate to the project directory.
                                                                                        Run the Flask application by executing the following command:
python app.py
The web application will start running on the local development server.                                                                                                         Open a web browser and visit http://localhost:5000 to access the image compression web interface.
                                                                                        Choose an image file using the provided file input field.
Click the "Compress" button to initiate the compression process.
Once the compression is complete, the compressed image will be downloaded automatically.
                                                                                        Code Overview                                                                           The Flask application is created using the Flask class from the flask module.
                                                                                        The root route ('/') serves the index.html file, which contains the web interface for image compression.
                                                                                        The /compress route handles the compression process. It accepts a POST request with an image file, compresses the image using the PIL library, and returns the compressed image for download.

The send_file function from Flask is used to send the compressed image as a response.

The app.run() statement starts the Flask development server.

Customize
You can customize the application according to your requirements. Here are some possible modifications:

Modify the index.html file to change the appearance and layout of the web interface.

Adjust the compression quality by modifying the quality parameter in the picture.save() function. Higher values (e.g., 70) result in better quality but larger file sizes.

Customize the MIME type and download filename by modifying the mimetype and download_name parameters in the send_file function.

Add additional error handling or validation logic to handle different scenarios.

License
This project is licensed under the MIT License. Feel free to modify and use it according to your needs.

Note: It's always a good practice to handle security and performance considerations when deploying a web application to a production environment.
