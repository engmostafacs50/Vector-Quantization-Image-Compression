import numpy as np
import numpy as np

from src.image_handler import (
    load_image,
    pad_image,
    image_to_blocks,
    blocks_to_vectors
)

from src.vector_quantization import (
    train_codebook,
    assign_clusters
)

def encode_labels(labels, k):
    bits_per_index = int(np.ceil(np.log2(k)))

    bitstream = ""

    for label in labels:
        binary = format(label, f"0{bits_per_index}b")
        bitstream += binary

    return bitstream

def pack_bits(bitstream):
    padding = (8 - len(bitstream) % 8) % 8

    bitstream += "0" * padding

    packed_data = int(bitstream, 2).to_bytes(
        len(bitstream) // 8,
        byteorder="big"
    )

    return packed_data, padding

def compress_image(
    image_path,
    block_height,
    block_width,
    k,
    max_iterations=100
):

    image = load_image(image_path)

    original_height, original_width = image.shape[:2]

    padded_image = pad_image(
        image,
        block_height,
        block_width
    )

    padded_height, padded_width = padded_image.shape[:2]

    blocks = image_to_blocks(
        padded_image,
        block_height,
        block_width
    )


    vectors = blocks_to_vectors(blocks)

    codebook = train_codebook(
        vectors,
        k,
        max_iterations
    )


    labels = assign_clusters(vectors, codebook)

    bitstream = encode_labels(labels, len(codebook))

    packed_data, padding = pack_bits(bitstream)

    metadata = {
        "original_height": original_height,
        "original_width": original_width,
        "padded_height": padded_height,
        "padded_width": padded_width,
        "block_height": block_height,
        "block_width": block_width,
        "channels": image.shape[2] if image.ndim == 3 else 1,
        "k": len(codebook),
        "num_vectors": len(vectors),
        "padding": padding
    }

    return {
        "codebook": codebook,
        "packed_data": packed_data,
        "metadata": metadata
    }