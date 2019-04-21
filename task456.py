# 4. Отберите все ссылки.
# 5. Ссылки на страницы какого домена встречаются чаще всего?
# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

import re
import frequency


with open('text.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    # вывод текста на экран
    print(text)

    # Отберите все ссылки.
    pattern_link = re.compile('\s([a-z0-9\.]*\.ru[/\w]*|[a-z0-9\.]*\.com[/\w]*)')
    links_list = pattern_link.findall(text)
    print(links_list)


    #поиск наиболее часто встречающегося домена
    list_domain = re.findall('[\.\s]([a-z0-9]+)\.ru', text)
    print('Ссылки на страницы этого домена встречаются чаще всего:')
    frequency.number(list_domain)

    #замена ссылок на текст
    text = pattern_link.sub('Ссылка отобразится после регистрации', text)
    print(text)