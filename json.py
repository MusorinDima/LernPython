import simplejson as js
friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': 'Leo', 'age': 33}
]
# тип объекта
print(type(friends))

# преобразуем список друзей в json
_json_friends = js.dumps(friends)

# печатаем что получилось
print(_json_friends)
# проверим тип
print(type(_json_friends))



# обратно из json в объект
friends = js.loads(_json_friends)

print(friends)
print(type(friends))

