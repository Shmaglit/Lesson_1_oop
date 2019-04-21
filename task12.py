# 1. Получите текст из файла.
# 2. Разбейте текст на предложения.

import re


with open('text.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    # вывод текста на экран
    print(text)

    # разбиение текста на предложения
    text2 = re.split('\.\s|!\s|\?\s', text)
    print(text2)

