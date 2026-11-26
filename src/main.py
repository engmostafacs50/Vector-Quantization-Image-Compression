from src.compression import compress_image, save_compressed_files
from src.decompression import decompress_image, load_compressed_files
from src.metrics import calculate_compression_ratio


def main():
    while True:
        print("\n===== Vector Quantization =====")
        print("1. Compress Image")
        print("2. Decompress Image")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            image_path = input("Enter image path: ")

            block_height = int(input("Enter block height: "))
            block_width = int(input("Enter block width: "))
            k = int(input("Enter codebook size: "))

            compressed_data = compress_image(
                image_path,
                block_height,
                block_width,
                k
            )

            save_compressed_files(
                compressed_data,
                "output/compressed"
            )

            ratio = calculate_compression_ratio(
                image_path,
                "output/compressed"
            )

            print("\nCompression completed!")
            print("Compression Ratio:", ratio)

        elif choice == "2":
            compressed_dir = input(
                "Enter compressed files directory: "
            )

            output_path = input(
                "Enter output image path: "
            )

            compressed_data = load_compressed_files(
                compressed_dir
            )

            decompress_image(
                compressed_data,
                output_path
            )

            print("\nDecompression completed!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()