from PIL import Image
import random

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = list(image.getdata())
    
    # Encrypt the pixels by applying a transformation using the key
    random.seed(key)
    random.shuffle(pixels)
    
    # Create a new image with the encrypted pixels
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    encrypted_pixels = list(image.getdata())
    
    # Decrypt the pixels by reversing the transformation using the key
    random.seed(key)
    indices = list(range(len(encrypted_pixels)))
    random.shuffle(indices)
    
    decrypted_pixels = [None] * len(encrypted_pixels)
    for i, idx in enumerate(indices):
        decrypted_pixels[idx] = encrypted_pixels[i]
    
    # Create a new image with the decrypted pixels
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

if __name__ == "__main__":
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? (Enter 'q' to quit): ").lower()
        
        if choice == 'e':
            input_image_path = input("Enter the path to the image to encrypt: ")
            output_image_path = input("Enter the path to save the encrypted image: ")
            key = input("Enter the encryption key: ")
            encrypt_image(input_image_path, output_image_path, key)
        elif choice == 'd':
            input_image_path = input("Enter the path to the encrypted image: ")
            output_image_path = input("Enter the path to save the decrypted image: ")
            key = input("Enter the decryption key: ")
            decrypt_image(input_image_path, output_image_path, key)
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
