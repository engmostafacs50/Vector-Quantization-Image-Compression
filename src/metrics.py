from pathlib import Path


def calculate_compression_ratio(original_path, compressed_dir):
    original_size = Path(original_path).stat().st_size

    compressed_dir = Path(compressed_dir)

    codebook_size = (compressed_dir / "codebook.npy").stat().st_size
    binary_size = (compressed_dir / "compressed.bin").stat().st_size
    metadata_size = (compressed_dir / "metadata.json").stat().st_size

    total_compressed_size = (
        codebook_size + binary_size + metadata_size
    )

    ratio = original_size / total_compressed_size

    return ratio