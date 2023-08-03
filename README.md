# Auto Image Cropper and Resizer

This Python script is designed to process images from a specified directory by removing the background, cropping them to only contain the main object, and then resizing them to multiple predefined sizes.

## Features

- **Background Removal**: Leveraging the power of the `rembg` library, it removes the background from images.
  
- **Auto Cropping**: This script uses OpenCV to detect the primary object in the image (non-white pixels) and then crops the image to tightly fit around this object.
  
- **Auto Resizing**: After cropping, the image is resized to three different sizes: 18x18, 36x36, and 72x72 pixels.

## Prerequisites

You must have the following installed:

- Python (version 3.7 or higher recommended)
  
- Libraries: `PIL`, `opencv-python`, `rembg`. You can install them via pip:
  
```bash
pip install Pillow opencv-python rembg

Usage
Clone this repository or download the script.

Update the DIRECTORY_PATH in the script to point to your directory containing the images you wish to process.

python
Copy code
DIRECTORY_PATH = 'C:\\path\\to\\your\\directory'
Run the script.
bash
Copy code
python script_name.py
After the script finishes, check the specified directory. You will find the processed images saved with their respective sizes in the filenames.

Note
Always keep a backup of your original images before running this script as the processing is irreversible.

Contributions
Feel free to fork this repository and make any improvements or adjustments you see fit. Any contributions are welcome!


Replace `script_name.py` with the actual name you've given to the script.
