$(document).ready(function() {
    // Входная последовательность
    let input = "abcdefghijklmno";

    // Разбиваем строку на группы по 4 символа
    let groups = input.match(/.{1,4}/g);

    // Подстановка для перестановки символов
    let substitution = [2, 0, 3, 1]; // Пример: переставляем символы в порядке 3-й, 1-й, 4-й, 2-й

    // Обрабатываем только четные группы (индексы 0, 2, 4 и т.д.)
    let result = groups.map((group, index) => {
        if (index % 2 === 0) { // Четные индексы
            let rearranged = "";
            substitution.forEach(pos => {
                if (pos < group.length) {
                    rearranged += group[pos];
                }
            });
            return rearranged;
        }
        return group; // Нечетные группы остаются без изменений
    });

    // Объединяем группы обратно в строку
    let output = result.join("");

    // Вывод результата
    console.log('Вывод результата 1 задание:', output);

    //_________________________________________________________________________________________________________

    // Функция для шифрования методом маршрутной перестановки
    function routePermutationEncrypt(text) {
        const rows = 5; // Количество строк
        const cols = 8; // Количество столбцов

        // Создаем таблицу 5x8 и заполняем её символами текста
        let table = [];
        let index = 0;
        for (let r = 0; r < rows; r++) {
            table[r] = [];
            for (let c = 0; c < cols; c++) {
                table[r][c] = index < text.length ? text[index] : 'X'; // Заполняем пустые ячейки 'X'
                index++;
            }
        }

        // Считываем текст по маршруту "змейка"
        let encryptedText = "";
        for (let c = 0; c < cols; c++) {
            if (c % 2 === 0) { // Четный столбец - сверху вниз
                for (let r = 0; r < rows; r++) {
                    encryptedText += table[r][c];
                }
            } else { // Нечетный столбец - снизу вверх
                for (let r = rows - 1; r >= 0; r--) {
                    encryptedText += table[r][c];
                }
            }
        }

        return encryptedText;
    }

    // Пример использования
    let inputText = "HELLOTHISISATESTMESSAGE";
    let encrypted = routePermutationEncrypt(inputText);

    // Вывод результата
    console.log("Зашифрованный текст 2 задание:", encrypted);

    //_________________________________________________________________________________________________________

    function scytaleEncrypt(text, columns) {
        // Определяем количество строк
        const rows = Math.ceil(text.length / columns);

        // Создаем таблицу (двумерный массив)
        let table = [];
        let index = 0;

        for (let r = 0; r < rows; r++) {
            table[r] = [];
            for (let c = 0; c < columns; c++) {
                // Заполняем таблицу символами текста, недостающие ячейки заполняем 'X'
                table[r][c] = index < text.length ? text[index] : 'X';
                index++;
            }
        }

        // Считываем текст по столбцам
        let encryptedText = "";
        for (let c = 0; c < columns; c++) {
            for (let r = 0; r < rows; r++) {
                encryptedText += table[r][c];
            }
        }

        return encryptedText;
    }

    // Пример использования
    let inputText = "HELLOTHISISATESTMESSAGE";
    let columns = 5; // Число столбцов
    let encrypted = scytaleEncrypt(inputText, columns);

    // Вывод результата
    console.log("Зашифрованный текст 3 задание:", encrypted);

    //_________________________________________________________________________________________________________

    // Функция для шифрования с использованием поворотной решетки
    function rotateGridEncrypt(text, gridSize, gridMask) {
        // Создаем квадратную таблицу
        let table = [];
        let index = 0;
        for (let r = 0; r < gridSize; r++) {
            table[r] = [];
            for (let c = 0; c < gridSize; c++) {
                table[r][c] = index < text.length ? text[index] : 'X'; // Заполняем пустые ячейки 'X'
                index++;
            }
        }

        // Функция для поворота решетки на 90 градусов
        function rotateGrid(gridMask) {
            let newMask = [];
            for (let [row, col] of gridMask) {
                newMask.push([col, gridSize - 1 - row]);
            }
            return newMask;
        }

        // Считываем текст через решетку
        let encryptedText = "";
        for (let i = 0; i < 4; i++) { // 4 поворота
            for (let [row, col] of gridMask) {
                encryptedText += table[row][col];
            }
            gridMask = rotateGrid(gridMask); // Поворачиваем решетку
        }

        return encryptedText;
    }

    // Пример использования
    let inputText = "HELLOTHISISATESTMESSAGE";
    let gridSize = 4; // Размер таблицы (4x4)
    let gridMask = [ // Решетка (координаты вырезанных ячеек)
        [0, 0], [1, 3], [2, 2], [3, 1]
    ];

    let encrypted = rotateGridEncrypt(inputText, gridSize, gridMask);

    // Вывод результата
    console.log("Зашифрованный текст 4 задание:", encrypted);

    //_________________________________________________________________________________________________________

    // Функция для шифрования методом двойной перестановки
    function doubleTranspositionEncrypt(text, rows, cols, rowKey, colKey) {
        // Создаем таблицу
        let table = [];
        let index = 0;

        for (let r = 0; r < rows; r++) {
            table[r] = [];
            for (let c = 0; c < cols; c++) {
                table[r][c] = index < text.length ? text[index] : 'X'; // Заполняем пустые ячейки 'X'
                index++;
            }
        }

        // Перестановка строк
        let rowPermutedTable = [];
        for (let i = 0; i < rows; i++) {
            rowPermutedTable[i] = table[rowKey[i]];
        }

        // Перестановка столбцов
        let finalTable = [];
        for (let r = 0; r < rows; r++) {
            finalTable[r] = [];
            for (let i = 0; i < cols; i++) {
                finalTable[r][i] = rowPermutedTable[r][colKey[i]];
            }
        }

        // Считываем зашифрованный текст построчно
        let encryptedText = "";
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                encryptedText += finalTable[r][c];
            }
        }

        return encryptedText;
    }

    // Пример использования
    let inputText = "HELLOTHISISATESTMESSAGE";
    let rows = 5; // Количество строк
    let cols = 5; // Количество столбцов
    let rowKey = [4, 2, 0, 3, 1]; // Ключ для перестановки строк
    let colKey = [3, 0, 4, 1, 2]; // Ключ для перестановки столбцов

    let encrypted = doubleTranspositionEncrypt(inputText, rows, cols, rowKey, colKey);

    // Вывод результата
    console.log("Зашифрованный текст 5 задание:", encrypted);

    //_________________________________________________________________________________________________________

    // Функция для генерации магического квадрата (размер n x n)
    function generateMagicSquare(n) {
        if (n % 2 === 0) {
            alert("Магический квадрат генерируется только для нечетных размеров!");
            return null;
        }

        let magicSquare = Array.from({ length: n }, () => Array(n).fill(0));
        let i = 0, j = Math.floor(n / 2); // Начальная позиция

        for (let num = 1; num <= n * n; num++) {
            magicSquare[i][j] = num;

            let newI = (i - 1 + n) % n; // Перемещение вверх
            let newJ = (j + 1) % n;     // Перемещение вправо

            if (magicSquare[newI][newJ] !== 0) {
                i = (i + 1) % n; // Если ячейка занята, перемещаемся вниз
            } else {
                i = newI;
                j = newJ;
            }
        }

        return magicSquare;
    }

    // Функция для шифрования текста с использованием магического квадрата
    function magicSquareEncrypt(text, n) {
        let magicSquare = generateMagicSquare(n);
        if (!magicSquare) return null;

        // Заполняем таблицу текстом
        let table = [];
        let index = 0;
        for (let i = 0; i < n; i++) {
            table[i] = [];
            for (let j = 0; j < n; j++) {
                table[i][j] = index < text.length ? text[index] : 'X'; // Заполняем пустые ячейки 'X'
                index++;
            }
        }

        // Считываем текст в порядке, заданном магическим квадратом
        let encryptedText = "";
        for (let num = 1; num <= n * n; num++) {
            for (let i = 0; i < n; i++) {
                for (let j = 0; j < n; j++) {
                    if (magicSquare[i][j] === num) {
                        encryptedText += table[i][j];
                    }
                }
            }
        }

        return encryptedText;
    }

    // Пример использования
    let inputText = "HELLOMAGICSQUARE";
    let size = 3; // Размер магического квадрата (3x3)
    let encrypted = magicSquareEncrypt(inputText, size);

    // Вывод результата
    console.log("Зашифрованный текст 6 задание:", encrypted);
});