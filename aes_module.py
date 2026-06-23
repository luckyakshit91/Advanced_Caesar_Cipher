from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'1234567890123456'


def aes_encrypt(message):
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    return encrypted.hex()


def aes_decrypt(ciphertext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), AES.block_size)
    return decrypted.decode()