from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_file(input_filename, output_filename, key):
    with open(input_filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Split the encrypted data into what we think is the IV/first block, and the rest
    supposed_iv_and_first_block = encrypted_data[:16]
    rest_of_encrypted_data = encrypted_data[16:]

    # Create an ECB cipher and decrypt just the first 16 bytes
    ecb_cipher = AES.new(key, AES.MODE_ECB)
    decrypted_first_block = ecb_cipher.decrypt(supposed_iv_and_first_block)

    # Create a CBC cipher using the first 16 bytes as the IV, and decrypt the rest of the data
    cbc_cipher = AES.new(key, AES.MODE_CBC, iv=supposed_iv_and_first_block)
    decrypted_rest = cbc_cipher.decrypt(rest_of_encrypted_data)
    #decrypted_rest = unpad(decrypted_rest, AES.block_size)

    # Concatenate the two decrypted parts
    full_decrypted_data = decrypted_first_block + decrypted_rest

    with open(output_filename, 'wb') as decrypted_file:
        decrypted_file.write(full_decrypted_data)

    print(f"Decryption completed. Decrypted content saved to {output_filename}.")

if __name__ == "__main__":
    input_filename = "encrypted_File.bin"
    output_filename = "decrypted_file3.txt"

    aes256_key = bytes([
        0x28, 0x8A, 0x2C, 0xFE, 0x3F, 0x75, 0xC4, 0x47,
        0xA5, 0x21, 0xC4, 0x5C, 0x33, 0x39, 0xE2, 0x64,
        0x2B, 0x34, 0x0F, 0x08, 0xD2, 0x37, 0x2A, 0x97,
        0x0D, 0x83, 0xA4, 0xD8, 0xB8, 0x01, 0x92, 0x2E
      ])

    decrypt_file(input_filename, output_filename, aes256_key)
