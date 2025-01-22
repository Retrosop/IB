using System;
using System.Text;

class TEMKEncryption
{
    // Пример ключа шифрования
    private static readonly string key = "ExampleKey123";

    // Метод шифрования
    public static string Encrypt(string message)
    {
        var encrypted = new StringBuilder();
        for (int i = 0; i < message.Length; i++)
        {
            // Пример шифрования: смещение символов на ключевое значение
            encrypted.Append((char)(message[i] + key[i % key.Length]));
        }
        return encrypted.ToString();
    }

    // Метод расшифровки
    public static string Decrypt(string encryptedMessage)
    {
        var decrypted = new StringBuilder();
        for (int i = 0; i < encryptedMessage.Length; i++)
        {
            // Обратное смещение символов на ключевое значение
            decrypted.Append((char)(encryptedMessage[i] - key[i % key.Length]));
        }
        return decrypted.ToString();
    }

    static void Main()
    {
        // Тестовое сообщение
        Console.WriteLine("Введите сообщение для шифрования:");
        string testMessage = Console.ReadLine();

        // Шифрование
        string encryptedMessage = Encrypt(testMessage);
        Console.WriteLine($"Зашифрованное сообщение: {encryptedMessage}");

        // Расшифровка
        string decryptedMessage = Decrypt(encryptedMessage);
        Console.WriteLine($"Расшифрованное сообщение: {decryptedMessage}");
    }
}