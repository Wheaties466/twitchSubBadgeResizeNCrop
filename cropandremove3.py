from rembg import remove
from PIL import Image
import cv2
import os
import io

# Define the directory path here
DIRECTORY_PATH = '[PUT_FULL_DIRECTORY_PATH_HERE]'

def remove_background_from_image_pil(img_pil):
    with io.BytesIO() as buffer:
        img_pil.save(buffer, format='PNG')
        input_image = buffer.getvalue()
        output_image = remove(input_image)
        return Image.open(io.BytesIO(output_image))

def crop_object_from_image(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    main_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(main_contour)
    cropped_img = img[y:y+h, x:x+w]
    return Image.fromarray(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))

def make_square(im, fill_color=(255, 255, 255)):
    x, y = im.size
    size = max(x, y)
    new_im = Image.new(im.mode, (size, size), fill_color)
    new_im.paste(im, ((size - x) // 2, (size - y) // 2))
    return new_im

def save_resized_images(image, base_filename, sizes):
    for size in sizes:
        resized_img = image.resize((size, size))
        no_bg_resized_img = remove_background_from_image_pil(resized_img)
        no_bg_resized_img.save(os.path.join(DIRECTORY_PATH, f"{base_filename}_{size}x{size}.png"))

def process_images():
    sizes = [18, 36, 72]
    
    for filename in os.listdir(DIRECTORY_PATH):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(DIRECTORY_PATH, filename)
            
            # Remove background and crop
            no_bg_image = remove_background_from_image_pil(Image.open(filepath))
            cropped_img = crop_object_from_image(filepath)
            square_img = make_square(cropped_img)
            
            # Save resized images
            base_filename, _ = os.path.splitext(filename)
            save_resized_images(square_img, base_filename, sizes)

if __name__ == '__main__':
    process_images()
