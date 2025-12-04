from PIL import Image
import struct

def rle_encode(data):
    if not data:
        return []

    encoded_data = []
    count = 1
    current_pixel = data[0]

    for i in range(1, len(data)):
        if data[i] == current_pixel:
            count += 1
        else:
            encoded_data.append((count, current_pixel))
            current_pixel = data[i]
            count = 1
    
    encoded_data.append((count, current_pixel))
    return encoded_data

def rle_decode(encoded_data):
    decoded_data = []
    for count, pixel in encoded_data:
        decoded_data.extend([pixel] * count)
    return decoded_data

try:
    # Path to your image
    image_path = r"C:\Users\mena.magdy\Desktop\python\ss\imges\macos-monterey-stock-black-dark-mode-layers-5k-6016x6016-5889.jpg  "
    compressed_file_path = "compressed_image.rle"
    decoded_image_path = "decoded_image.png"

    # Open the image and convert to grayscale
    with Image.open(image_path) as img:
        grayscale_img = img.convert('L')
        pixel_data = list(grayscale_img.getdata())
        width, height = grayscale_img.size

        # Encode the pixel data
        print("Encoding image...")
        encoded_pixel_data = rle_encode(pixel_data)

        # Save the encoded data to a file
        print(f"Saving encoded data to '{compressed_file_path}'...")
        with open(compressed_file_path, 'wb') as f:
            # Write width and height as 4-byte integers
            f.write(struct.pack('II', width, height))
            for count, pixel in encoded_pixel_data:
                # Write count and pixel as bytes
                f.write(struct.pack('IB', count, pixel))
        
        print("Encoded data saved.")

        # Read the encoded data from the file
        print(f"Reading encoded data from '{compressed_file_path}'...")
        with open(compressed_file_path, 'rb') as f:
            # Read width and height
            width, height = struct.unpack('II', f.read(8))
            read_encoded_data = []
            while True:
                data = f.read(5) # Read 5 bytes (4 for count, 1 for pixel)
                if not data:
                    break
                count, pixel = struct.unpack('IB', data)
                read_encoded_data.append((count, pixel))
        
        print("Encoded data read.")

        # Decode the pixel data
        print("Decoding image...")
        decoded_pixel_data = rle_decode(read_encoded_data)

        # Create a new image from the decoded data
        print(f"Saving decoded image to '{decoded_image_path}'...")
        if len(decoded_pixel_data) == width * height:
            decoded_image = Image.new('L', (width, height))
            decoded_image.putdata(decoded_pixel_data)
            decoded_image.save(decoded_image_path)
            print("Decoded image saved.")
        else:
            print("Error: Decoded data length does not match image dimensions.")


        # Verify the compression
        if pixel_data == decoded_pixel_data:
            print("\nCompression and decompression successful!")
        else:
            print("\nError: Decoded data does not match original data.")

except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
