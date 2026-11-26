import numpy as np
from src.image_handler import (
    pad_image,
    image_to_blocks,
    blocks_to_vectors
)

def test_image_pipeline():
    image = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    padded = pad_image(image, 2, 2)
    blocks = image_to_blocks(padded, 2, 2)
    vectors = blocks_to_vectors(blocks)

    assert padded.shape == (4, 4)
    assert blocks.shape == (4, 2, 2)
    assert vectors.shape == (4, 4)

    print(vectors)