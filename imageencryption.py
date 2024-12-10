from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key=10):
  
    image = Image.open(image_path)
    image_data = np.array(image)

    
    encrypted_data = (image_data + key) % 256 

    image_dir = os.path.dirname(image_path)
    encrypted_image_path = os.path.join(image_dir, "encrypted_image.png")
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save(encrypted_image_path)
    
    print(f"Encryption complete. Saved as '{encrypted_image_path}'")
    
def decrypt_image(encrypted_image_path, key=10):
   
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_data = np.array(encrypted_image)

    decrypted_data = (encrypted_data - key) % 256  

    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    

    decrypted_image.save("decrypted_image.png")
    print("Decryption complete. Saved as 'decrypted_image.png'")
    
if __name__ == "__main__":

    original_image_path = r"C:\Users\Acer\Desktop\project 2\images\image1.jpg"
  
    encrypt_image(original_image_path, key=10)

\
    decrypt_image(r"C:\Users\Acer\Desktop\project 2\images\encrypted_image.png", key=10)
