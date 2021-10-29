person = {'name':'Max', 'phones': [123,345]}
# откроем файл
with open('person.dat','wb') as f:
    #  например запишем объект в файл построчно
    name = person['name']
    # переводим в байты
    f.write(f'{name}\n' .encode('utf-8'))
    phones = person['phones']
    # запишем 1 телефон вт новую строку
    for phone in phones:
        f.write(f'{phone}\n' .encode('utf-8'))

print('объект записан')
