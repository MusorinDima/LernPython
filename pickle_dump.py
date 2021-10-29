import _pickle

person = {'name': 'Max', 'phones': [123, 345], 'age': 20}

# открываем файл
with open('person.dat', 'wb') as f:
    # сразу пишем объект целиком с помощью pickle
    _pickle.dump(person, f)

print('Объект записан')