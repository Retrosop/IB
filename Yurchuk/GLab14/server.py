import socket
import struct
import time
from common import decrypt_data, create_hmac, encrypt_data


def server(host='127.0.0.1', port=12345):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        conn, addr = sock.accept()
        print(f"Подключение от {addr}")
        try:
            # Получение данных
            data = conn.recv(4096)
            if not data:
                break

            # Расшифровка сообщения
            timestamp, iv, ciphertext, hmac = struct.unpack('<Q12s128s32s', data)
            key = b'session_key_placeholder'  # В реальной реализации используйте KDF
            decrypted_command = decrypt_data(key, ciphertext, iv)

            # Проверка временной метки и HMAC
            # TODO: Проверить HMAC и timestamp

            # Обработка команды
            response = f"Команда '{decrypted_command.decode()}' выполнена успешно".encode()

            # Отправка зашифрованного ответа
            encrypted_response = encrypt_data(key, response, iv)
            conn.send(encrypted_response)

        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

server()
