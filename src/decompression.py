import numpy as np
from PIL import Image
from pathlib import Path
import json
from src.image_handler import (
    vectors_to_blocks,
    blocks_to_image,
    crop_image
)

def unpack_bits(packed_data):
    bitstream = ""

    for byte in packed_data:
        binary = format(byte, "08b")
        bitstream += binary

    return bitstream



def decode_labels(bitstream, k, padding=0):
    if padding > 0:
        bitstream = bitstream[:-padding]

    bits_per_index = int(np.ceil(np.log2(k)))

    labels = []

    for i in range(0, len(bitstream), bits_per_index):
        binary = bitstream[i:i + bits_per_index]

        label = int(binary, 2)

        labels.append(label)

    return np.array(labels)


def decode_vectors(labels, codebook):
    vectors = codebook[labels]

    return vectors

def decompress_image(compressed_data, output_path):

    codebook = compressed_data["codebook"]
    packed_data = compressed_data["packed_data"]
    metadata = compressed_data["metadata"]


    bitstream = unpack_bits(packed_data)

    labels = decode_labels(
        bitstream,
        metadata["k"],
        metadata["padding"]
    )


    vectors = decode_vectors(labels, codebook)


    blocks = vectors_to_blocks(
        vectors,
        metadata["block_height"],
        metadata["block_width"],
        metadata["channels"]
    )


    reconstructed_image = blocks_to_image(
        blocks,
        metadata["padded_height"],
        metadata["padded_width"],
        metadata["block_height"],
        metadata["block_width"]
    )


    reconstructed_image = crop_image(
        reconstructed_image,
        metadata["original_height"],
        metadata["original_width"]
    )

    reconstructed_image = np.clip(
        np.rint(reconstructed_image),
        0,
        255
    ).astype(np.uint8)


    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    Image.fromarray(reconstructed_image).save(output_path)

    return reconstructed_image


def load_compressed_files(input_dir):
    input_dir = Path(input_dir)

    # Load Codebook
    codebook = np.load(input_dir / "codebook.npy")

    # Load Binary Stream
    with open(input_dir / "compressed.bin", "rb") as file:
        packed_data = file.read()

    # Load Metadata
    with open(input_dir / "metadata.json", "r") as file:
        metadata = json.load(file)

    return {
        "codebook": codebook,
        "packed_data": packed_data,
        "metadata": metadata
    }