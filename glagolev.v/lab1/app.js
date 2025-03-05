// Функция для шифрования текста с использованием шифра "Сцитала"
function encryptScytale(text, columns) {
  // Убираем пробелы и приводим текст к верхнему регистру
  const cleanText = text.replace(/\s+/g, "").toUpperCase();

  // Создаем массив строк (шифрующая таблица)
  const rows = Math.ceil(cleanText.length / columns);
  const table = Array.from({ length: rows }, () => []);

  // Заполняем таблицу символами текста
  for (let i = 0; i < cleanText.length; i++) {
    const row = Math.floor(i / columns);
    const col = i % columns;
    table[row][col] = cleanText[i];
  }

  // Читаем символы по столбцам для получения зашифрованного текста
  let encryptedText = "";
  for (let col = 0; col < columns; col++) {
    for (let row = 0; row < rows; row++) {
      if (table[row][col]) {
        encryptedText += table[row][col];
      }
    }
  }

  return encryptedText;
}

// Функция для расшифровки текста с использованием шифра "Сцитала"
function decryptScytale(encryptedText, columns) {
  const rows = Math.ceil(encryptedText.length / columns);
  const table = Array.from({ length: rows }, () => []);

  // Заполняем таблицу символами зашифрованного текста по столбцам
  let index = 0;
  for (let col = 0; col < columns; col++) {
    for (let row = 0; row < rows; row++) {
      if (index < encryptedText.length) {
        table[row][col] = encryptedText[index];
        index++;
      }
    }
  }

  // Читаем символы по строкам для получения расшифрованного текста
  let decryptedText = "";
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < columns; col++) {
      if (table[row][col]) {
        decryptedText += table[row][col];
      }
    }
  }

  return decryptedText;
}

// Пример использования
const text = "Сцитала это древний шифр";
const columns = 5;

console.log("Исходный текст:", text);

// Шифрование
const encrypted = encryptScytale(text, columns);
console.log("Зашифрованный текст:", encrypted);

// Расшифровка
const decrypted = decryptScytale(encrypted, columns);
console.log("Расшифрованный текст:", decrypted);
