# подсчет частоты повторения слов

def number(word_list):
    frequency_var = {}
    for word in word_list:
        count = frequency_var.get(word, 0)
        frequency_var[word] = count + 1

    # вывод чаще повторяющихся
    for key in frequency_var:
        if frequency_var[key] == max(frequency_var.values()):
            print(key, frequency_var[key])

#list = ['rte', 'hghg', 'rte', 'jhhj']
#frequency(list)
