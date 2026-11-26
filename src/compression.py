import numpy as np

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

