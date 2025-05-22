import os
from PIL import Image
from django.conf import settings

def resize_image(image, new_width):
    img_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
    img_pil = Image.open(img_full_path)
    original_width, original_height = img_pil.size
    
    if original_width <= new_width:
        img_pil.close()
        return
    
    new_height = round((new_width / original_width) * original_height)
    
    new_img = img_pil.resize((new_width, new_height), Image.LANCZOS) # type: ignore
    new_img.save(img_full_path, optimize=True, quality=50)
    # print(f"Image resized to {new_width}x{new_height} and saved at {img_full_path}")
    
    