def permute_blocks(text, block_size=4, permutation=(2, 0, 3, 1)):
    """
    Разбивает текст на блоки по block_size символов и переставляет символы в соответствии с permutation.
    """
    blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    
    permuted_blocks = []
    for block in blocks:
        if len(block) < block_size:
            # Если последний блок короче, применяем перестановку только к существующим символам
            permuted_block = ''.join(block[i] for i in permutation if i < len(block))
        else:
            permuted_block = ''.join(block[i] for i in permutation)
        
        permuted_blocks.append(permuted_block)
    
    return ''.join(permuted_blocks)

# Пример использования
cipher_text = "шифртекст"  # Исходный текст
result = permute_blocks(cipher_text)
print("Результат перестановки:", result)
