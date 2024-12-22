from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.hashes import Hash, SM3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

# Генерация ключа с помощью Scrypt
def generate_key(salt, password, length=32):
    kdf = Scrypt(salt=salt, length=length, n=2**14, r=8, p=1, backend=default_backend())
    return kdf.derive(password)

# Создание HMAC на основе SM3
def create_hmac(key, message):
    h = Hash(SM3(), backend=default_backend())
    h.update(message)
    return h.finalize()

# Шифрование с ChaCha20
def encrypt_data(key, plaintext, iv):
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext)

# Расшифровка с ChaCha20
def decrypt_data(key, ciphertext, iv):
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)