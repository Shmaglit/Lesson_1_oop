# 3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
import re
import frequency

with open('text.txt', 'r', encoding = 'utf-8') as f:

    #вывод всех слов из текста
    text = f.read().lower()
    list_words=re.findall('\s([а-я]{4,15})[\s\.,!\?]', text)
    print(list)
    # вывод чаще повторяющихся
    frequency.number(list_words)

