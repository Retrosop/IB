import socket
import struct
import time
from common import encrypt_data, create_hmac
import os

def client(server_ip, server_port, command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))

    try:
        # Формирование сообщения
        timestamp = struct.pack('<Q', int(time.time()))
        iv = os.urandom(12)
        key = b'session_key_placeholder'  # В реальной реализации используйте KDF
        encrypted_command = encrypt_data(key, command.encode(), iv)
        hmac = create_hmac(key, timestamp + iv + encrypted_command)

        # Отправка сообщения
        message = timestamp + iv + encrypted_command + hmac
        sock.send(message)

        # Получение ответа
        encrypted_response = sock.recv(4096)
        decrypted_response = encrypt_data(key, encrypted_response, iv)

        print(f"Ответ сервера: {decrypted_response.decode()}")
    finally:
        sock.close()

client('127.0.0.1', 12345, '{"command_number": 1, "command_body": "dir"}')