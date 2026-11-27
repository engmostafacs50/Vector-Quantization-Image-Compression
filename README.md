# Vector Quantization - Image Compression .

A Python implementation of Vector Quantization for image compression and decompression.

## Project Requirements

The project allows users to compress and decompress images using Vector Quantization.

### Compression Input

- Input image.
- Block/Vector dimensions.
- Number of vectors in the Codebook.

### Compression Output

- Codebook file.
- Compressed image file (Binary Stream).

### Decompression Input

- Codebook file.
- Compressed image file (Binary Stream).

### Decompression Output

- Reconstructed image.

## Main Features

- Image compression using Vector Quantization.
- Image decompression.
- User-defined block dimensions.
- User-defined Codebook size.
- Automatic image padding when necessary.
- Binary stream generation.
- Codebook file generation.
- Compression Ratio calculation.
- User interface for selecting compression or decompression.

## Technologies

- Python
- NumPy
- Pillow

## Installation

```bash
git clone https://github.com/engmostafacs50/Vector-Quantization-Image-Compression.git
cd Vector-Quantization
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python -m src.main
```

The user can choose between:

1. Compression
2. Decompression

### Compression

The user provides:
- Image path.
- Block dimensions.
- Codebook size.

The application generates:
- Codebook file.
- Compressed binary stream.

### Decompression

The user provides:
- Codebook file.
- Compressed binary stream.

The application reconstructs and saves the image.

## Compression Ratio

The Compression Ratio is calculated as:

\[
CR = \frac{\text{Original Image Size}}{\text{Compressed Data Size}}
\]

The compressed data size includes the Codebook and Binary Stream.

## Project Structure

```text
src/
├── main.py
├── compression.py
├── decompression.py
├── vector_quantization.py
├── image_handler.py
└── metrics.py

tests/
examples/
output/
```
