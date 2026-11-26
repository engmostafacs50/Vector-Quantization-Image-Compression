import numpy as np

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