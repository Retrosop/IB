from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def triple_des_encrypt(plaintext, key1, key2, key3):
    # Создаем объекты шифра для каждого ключа
    cipher1 = DES.new(key1, DES.MODE_ECB)
    cipher2 = DES.new(key2, DES.MODE_ECB)
    cipher3 = DES.new(key3, DES.MODE_ECB)

    # Шифрование
    padded_text = pad(plaintext, DES.block_size)
    encrypted = cipher1.encrypt(padded_text)
    decrypted = cipher2.decrypt(encrypted)
    final_encrypted = cipher3.encrypt(decrypted)

    return final_encrypted


def triple_des_decrypt(ciphertext, key1, key2, key3):
    # Создаем объекты шифра для каждого ключа
    cipher1 = DES.new(key1, DES.MODE_ECB)
    cipher2 = DES.new(key2, DES.MODE_ECB)
    cipher3 = DES.new(key3, DES.MODE_ECB)

    # Расшифрование
    decrypted = cipher3.decrypt(ciphertext)
    encrypted = cipher2.encrypt(decrypted)
    final_decrypted = cipher1.decrypt(encrypted)

    return unpad(final_decrypted, DES.block_size)


# Пример использования
plaintext = b"This is a secret message."
key1 = b'12345678'
key2 = b'23456789'
key3 = b'34567890'

ciphertext = triple_des_encrypt(plaintext, key1, key2, key3)
print("Encrypted:", ciphertext)

decrypted_text = triple_des_decrypt(ciphertext, key1, key2, key3)
print("Decrypted:", decrypted_text.decode())
