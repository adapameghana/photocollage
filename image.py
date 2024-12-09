from PIL import Image
import os
from math import ceil, sqrt

def create_photo_collage(image_folder, output_path, collage_width, collage_height, margin=10):
    """
    Generate a photo collage from images in a folder.

    :param image_folder: Path to the folder containing images.
    :param output_path: Path to save the output collage.
    :param collage_width: Width of the collage in pixels.
    :param collage_height: Height of the collage in pixels.
    :param margin: Margin between images in pixels.
    """
    # Check if the folder exists
    if not os.path.exists(image_folder):
        print(f"Error: The folder '{image_folder}' does not exist.")
        return

    # Get all image file paths from the folder
    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) 
                   if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

    if not image_files:
        print("No images found in the specified folder.")
        return

    # Determine grid size (number of images per row and column)
    num_images = len(image_files)
    grid_size = ceil(sqrt(num_images))  # Number of rows and columns
    thumb_width = (collage_width - (grid_size + 1) * margin) // grid_size
    thumb_height = (collage_height - (grid_size + 1) * margin) // grid_size

    # Create a blank canvas for the collage
    collage = Image.new("RGB", (collage_width, collage_height), "white")

    # Process and paste each image onto the collage
    x_offset = margin
    y_offset = margin
    for idx, image_file in enumerate(image_files):
        try:
            with Image.open(image_file) as img:
                # Resize image to thumbnail size
                img.thumbnail((thumb_width, thumb_height))
                collage.paste(img, (x_offset, y_offset))

                # Update offsets
                x_offset += thumb_width + margin
                if (idx + 1) % grid_size == 0:  # Move to the next row
                    x_offset = margin
                    y_offset += thumb_height + margin
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    # Save the final collage
    collage.save(output_path)
    print(f"Collage saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Replace with the actual folder containing your images
    image_folder = "C:/Users/adapa/Downloads/images"  
    output_path = "photo_collage1.jpg"  # Replace with the desired output path
    collage_width = 1000  # Width of the collage
    collage_height = 1000  # Height of the collage

    create_photo_collage(image_folder, output_path, collage_width, collage_height)
