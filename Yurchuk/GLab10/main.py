from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt_cbc(data, key):
    iv = get_random_bytes(DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, DES.block_size))
    return iv + encrypted_data

def des_decrypt_cbc(encrypted_data, key):
    iv = encrypted_data[:DES.block_size]
    encrypted_data = encrypted_data[DES.block_size:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
    return decrypted_data

# Ввод данных с клавиатуры
data = input("Введите текст для шифрования: ").encode('utf-8')

# Ввод ключа с клавиатуры (должен быть 8 байт)
key_input = input("Введите ключ (8 символов): ")
if len(key_input) != 8:
    raise ValueError("Ключ должен быть ровно 8 символов!")
key = key_input.encode('utf-8')

# Шифрование
encrypted_data = des_encrypt_cbc(data, key)
print("Зашифрованные данные:", encrypted_data)

# Расшифрование
decrypted_data = des_decrypt_cbc(encrypted_data, key)
print("Расшифрованные данные:", decrypted_data.decode('utf-8'))