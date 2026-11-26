from src.compression import encode_labels
from src.compression import pack_bits


def test_encode_labels():
    labels = [0, 0, 1, 1]

    bitstream = encode_labels(labels, 2)

    assert bitstream == "0011"
    print(bitstream)
    
def test_pack_bits():
    bitstream = "00110110"

    packed_data, padding = pack_bits(bitstream)

    print("Packed:", packed_data)
    print("Padding:", padding)

    assert packed_data == b"\x36"
    assert padding == 0
    
