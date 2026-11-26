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

def image_to_blocks(image, block_height, block_width):
    height , width = image.shape[0 : 2]
    
    blocks = []
    
    for i in range(0 , height , block_height) :
        for j in range(0 , width , block_width) :
            block = image[
                i : i + block_height , j : j + block_width
            ]
            blocks.append(block)
    return np.array(blocks)

def blocks_to_vectors(blocks):
    number_of_blocks = len(blocks)

    vectors = blocks.reshape(number_of_blocks, -1)

    return vectors


def vectors_to_blocks(vectors, block_height, block_width, channels=1):

    if channels == 1:
        blocks = vectors.reshape(
            len(vectors),
            block_height,
            block_width
        )
    else:
        blocks = vectors.reshape(
            len(vectors),
            block_height,
            block_width,
            channels
        )

    return blocks


def blocks_to_image(blocks, padded_height, padded_width,
                    block_height, block_width):

    blocks_per_row = padded_width // block_width

    channels = blocks.shape[-1] if blocks.ndim == 4 else None

    if channels is None:
        image = np.zeros(
            (padded_height, padded_width),
            dtype=blocks.dtype
        )
    else:
        image = np.zeros(
            (padded_height, padded_width, channels),
            dtype=blocks.dtype
        )

    for index, block in enumerate(blocks):

        row = index // blocks_per_row
        col = index % blocks_per_row

        start_row = row * block_height
        start_col = col * block_width

        image[
            start_row:start_row + block_height,
            start_col:start_col + block_width
        ] = block

    return image


def crop_image(image, original_height, original_width):
    cropped_image = image[:original_height, :original_width]

    return cropped_image