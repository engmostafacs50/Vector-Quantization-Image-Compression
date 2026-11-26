from PIL import Image
import numpy as np

image = np.random.randint(
    0, 256,
    size=(128, 128, 3),
    dtype=np.uint8
)

Image.fromarray(image).save(
    "examples/sample_images/test.png"
)

from src.compression import compress_image

result = compress_image(
    image_path="examples/sample_images/test.png",
    block_height=2,
    block_width=2,
    k=4,
    max_iterations=10
)

print("Compression completed!")
print("Codebook:")
print(result["codebook"])

print("Metadata:")
print(result["metadata"])