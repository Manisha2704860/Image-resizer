from PIL import Image
import os

# Define the input folder path and output size
input_folder = 'C:\\Users\\MANISHA\\OneDrive\\Pictures\\Screenshots'
output_folder = 'C:\\Users\\MANISHA\\OneDrive\\Pictures\\Saved Pictures'
output_size = (600, 600)  # Example size

# Create output folder if it doesn't exist 
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Resize the image
        img = img.resize(output_size)
        
        # Save the resized image to output folder
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print("Batch image resizing completed.")