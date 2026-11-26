from PIL import Image
import numpy as np

from src.compression import compress_image, save_compressed_files
from src.decompression import decompress_image, load_compressed_files
from src.metrics import calculate_compression_ratio
# Create test image
image = np.random.randint(
    0, 256,
    size=(128, 128, 3),
    dtype=np.uint8
)

Image.fromarray(image).save(
    "examples/sample_images/test.png"
)

# Compression
compressed_data = compress_image(
    "examples/sample_images/test.png",
    block_height=2,
    block_width=2,
    k=4
)

save_compressed_files(
    compressed_data,
    "output/compressed"
)

print("Compression completed!")

# Load compressed files
loaded_data = load_compressed_files("output/compressed")
ratio = calculate_compression_ratio(
    "examples/sample_images/test.png",
    "output/compressed"
)

print("Compression Ratio:", ratio)
# Decompression
reconstructed_image = decompress_image(
    loaded_data,
    "output/reconstructed.png"
)

print("Decompression completed!")
print("Reconstructed shape:", reconstructed_image.shape)