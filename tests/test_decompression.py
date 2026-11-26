from src.decompression import decode_labels


def test_decode_labels():
    bitstream = "00011011"

    labels = decode_labels(bitstream, k=4)

    expected = [0, 1, 2, 3]

    assert labels.tolist() == expected  
    