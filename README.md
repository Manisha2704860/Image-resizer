# Image-resizer

# What i built ?

You built a Python script that uses the Pillow library to batch resize images. The script takes a folder of images as input, resizes each image to a specified size (800x600), and saves the resized images to a new folder.

# Why i built it ?

I likely built this script to automate the process of resizing multiple images to a uniform size, which can be useful for various purposes such as web development, graphic design, or data processing.

# How it works :

1. Importing libraries: The script imports the Image class from the Pillow library and the os module for working with file paths and directories.
2. Defining input and output folders: The script specifies the input folder containing the images to be resized and the output folder where the resized images will be saved.
3. Defining output size: The script sets the desired output size for the resized images (800x600).
4. Creating output folder: If the output folder doesn't exist, the script creates it using os.makedirs().
5. Looping through images: The script loops through each file in the input folder and checks if it's an image file (based on the file extension).
6. Resizing images: For each image file, the script opens the image using Image.open(), resizes it using img.resize(), and saves the resized image to the output folder using img.save().
