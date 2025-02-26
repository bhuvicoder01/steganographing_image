from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import secrets
import pyperclip

# Encryption/Decryption Functions
def encrypt_message(message, key):
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(encrypted_message, key):
    backend = default_backend()
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_data) + unpadder.finalize()
    return message.decode()

# Steganography Functions
def embed_message(image_path, encrypted_message, output_path):
    img = Image.open(image_path).convert('RGB')
    img_array = np.array(img)
    max_bytes = img_array.size // 8
    message_length = len(encrypted_message)
    if message_length > max_bytes:
        raise ValueError(f"Message too large. Max capacity: {max_bytes} bytes.")
    binary_message = ''.join(format(byte, '08b') for byte in encrypted_message)
    binary_message += '1111111111111111'
    flat_array = img_array.flatten()
    for i in range(len(binary_message)):
        flat_array[i] = (flat_array[i] & 0xFE) | int(binary_message[i])
    stego_array = flat_array.reshape(img_array.shape)
    stego_img = Image.fromarray(stego_array)
    stego_img.save(output_path)
    return output_path

def extract_message(stego_image_path):
    stego_img = Image.open(stego_image_path).convert('RGB')
    stego_array = np.array(stego_img)
    flat_array = stego_array.flatten()
    binary_message = ''
    for pixel in flat_array:
        binary_message += str(pixel & 1)
        if binary_message[-16:] == '1111111111111111':
            break
    message_bytes = [int(binary_message[i:i+8], 2) for i in range(0, len(binary_message) - 16, 8)]
    return bytes(message_bytes)

# Key Generation Function
def generate_key():
    """
    Generate a random 32-byte key for AES-256 encryption.
    Returns:
        bytes: A 32-byte key.
    """
    return secrets.token_bytes(32)

# GUI Class
class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Steganography Tool")
        self.root.geometry("500x400")
        
        # GUI Components
        tk.Label(root, text="Select Image:").pack(pady=5)
        self.button_select = tk.Button(root, text="Browse", command=self.select_image)
        self.button_select.pack()
        
        tk.Label(root, text="Message:").pack(pady=5)
        self.entry_message = tk.Entry(root, width=50)
        self.entry_message.pack()
        
        tk.Label(root, text="Encryption Key (32 bytes):").pack(pady=5)
        self.entry_key = tk.Entry(root, width=50)
        self.entry_key.pack()
        
        self.button_generate_key = tk.Button(root, text="Generate Key", command=self.generate_and_copy_key)
        self.button_generate_key.pack(pady=5)
        
        self.button_copy_key = tk.Button(root, text="Copy Key", command=self.copy_key)
        self.button_copy_key.pack(pady=5)
        
        self.button_embed = tk.Button(root, text="Embed Message", command=self.embed)
        self.button_embed.pack(pady=10)
        
        self.button_extract = tk.Button(root, text="Extract Message", command=self.extract)
        self.button_extract.pack(pady=5)
        
        self.image_path = None
    
    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp")])
        if self.image_path:
            messagebox.showinfo("Selected", f"Image: {os.path.basename(self.image_path)}")
    
    def generate_and_copy_key(self):
        key = generate_key()
        key_hex = key.hex()  # Display as hex for readability
        self.entry_key.delete(0, tk.END)
        self.entry_key.insert(0, key_hex)
        pyperclip.copy(key_hex)
        messagebox.showinfo("Key Generated", "A new 32-byte key has been generated and copied to clipboard.")
    
    def copy_key(self):
        key_text = self.entry_key.get()
        if key_text:
            pyperclip.copy(key_text)
            messagebox.showinfo("Key Copied", "Key copied to clipboard.")
        else:
            messagebox.showerror("Error", "No key to copy.")
    
    def embed(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image.")
            return
        message = self.entry_message.get()
        key_input = self.entry_key.get()
        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return
        if len(key_input) == 64 and all(c in '0123456789abcdefABCDEF' for c in key_input):
            key = bytes.fromhex(key_input)  # Convert hex string to bytes
        else:
            key = key_input.encode()
            if len(key) != 32:
                messagebox.showerror("Error", "Key must be exactly 32 bytes.")
                return
        
        try:
            encrypted_message = encrypt_message(message, key)
            output_path = "stego_" + os.path.basename(self.image_path)
            embed_message(self.image_path, encrypted_message, output_path)
            messagebox.showinfo("Success", f"Message embedded. Saved as {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def extract(self):
        stego_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp")])
        if not stego_image_path:
            return
        key_input = self.entry_key.get()
        if len(key_input) == 64 and all(c in '0123456789abcdefABCDEF' for c in key_input):
            key = bytes.fromhex(key_input)  # Convert hex string to bytes
        else:
            key = key_input.encode()
            if len(key) != 32:
                messagebox.showerror("Error", "Key must be exactly 32 bytes.")
                return
        
        try:
            encrypted_message = extract_message(stego_image_path)
            decrypted_message = decrypt_message(encrypted_message, key)
            messagebox.showinfo("Extracted Message", decrypted_message)
        except Exception as e:
            messagebox.showerror("Error", f"Extraction failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()