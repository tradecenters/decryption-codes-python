from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad
import base64

# Input values (placeholders, replace with actual values)
base64_key = "YOUR_BASE64_KEY_HERE"
base64_encrypted = "YOUR_BASE64_ENCRYPTED_DATA"

# Decode Base64 key and encrypted data
key_bytes = base64.b64decode(base64_key)
encrypted_bytes = base64.b64decode(base64_encrypted)

# Create 3DES cipher in ECB mode
cipher = DES3.new(key_bytes, DES3.MODE_ECB)

# Decrypt and unpad the result
decrypted_padded = cipher.decrypt(encrypted_bytes)
decrypted = unpad(decrypted_padded, DES3.block_size)

# Convert to string
print("Decrypted Trade JSON data:", decrypted.decode('utf-8'))
