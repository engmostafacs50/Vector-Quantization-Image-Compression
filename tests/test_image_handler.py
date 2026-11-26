import numpy as np
from src.image_handler import pad_image


def test_padding():
    image = np.ones((7, 7))

    padded = pad_image(image, 3, 3)

    assert padded.shape == (9, 9)

    print("Padding Test Passed!")