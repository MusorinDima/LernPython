# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    f.write(b'hello bytes')

# читаем как текст
with open('bytes.txt', 'r', encoding='ascii') as f:
    #     пишем строку байт
    print(f.read())

# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    #     пишем строку байт
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

# читаем как текст с кодировкой utf-8
with open('bytes.txt', 'r', encoding='utf-8') as f:
    #     пишем строку байт
    print(f.read())