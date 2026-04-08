import os
from PIL import Image

def create_dino_gif(folder_path, output_name, right_crop_offset, duration_ms):
    images = []
    
    # Get all PNG files and sort them to keep your sequence in order
    filenames = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

    for filename in filenames:
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            # Get dimensions
            width, height = img.size
            
            # Crop logic: (left, upper, right, lower)
            # We subtract the offset from the total width to trim the right side
            new_width = width - right_crop_offset
            cropped_img = img.crop((0, 0, new_width, height))
            
            # Convert to RGB if necessary (GIFs handle transparency differently)
            images.append(cropped_img.convert("RGBA"))

    if images:
        # Save as GIF
        # duration is in milliseconds, so 4 seconds = 4000ms
        images[0].save(
            output_name,
            save_all=True,
            append_images=images[1:],
            duration=duration_ms,
            loop=0
        )
        print(f"Success! {output_name} created with {len(images)} frames.")
    else:
        print("No PNG files found in the directory.")

# --- Configuration ---
folder = './'          # Path to your image folder
output = 'dino_slideshow.gif'  # Output filename
crop_offset = 160               # Pixels to remove from the right border
delay = 4000                   # 4 seconds in milliseconds

create_dino_gif(folder, output, crop_offset, delay)