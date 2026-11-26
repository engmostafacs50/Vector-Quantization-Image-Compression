from PIL import Image
import numpy as np


def load_image(image_path):
    image = Image.open(image_path)

    if image.mode == "L":
        image = image.convert("L")
    else:
        image = image.convert("RGB")

    return np.array(image)


def pad_image(image , block_height , block_width) :
    
        if block_height <= 0 or block_width <= 0:
            raise ValueError("Block dimensions must be positive.")
        
        height , width = image.shape[:2] # image.shape --> (height , width , #channales if image is RGB)
        pad_height = (block_height - height % block_height) % block_height
        pad_width = (block_width - width % block_width) % block_width
        
        if image.ndim == 2 : 
            padding = (
            (0, pad_height),
            (0, pad_width)
        )
        else:
            padding = (
            (0, pad_height),
            (0, pad_width),
            (0, 0)
        )
            
        padded_image = np.pad(image,padding,mode="constant",constant_values=0)
        
        return padded_image 
