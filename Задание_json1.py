import simplejson as json
import _pickle
my_favourite_group = {
'name': 'Г.М.О.',
'треки': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}

js_group = json.dumps(my_favourite_group)
# print(js_group)

pick_group = _pickle.dumps(my_favourite_group)
# print(pick_group)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    _pickle.dump(my_favourite_group, f)
