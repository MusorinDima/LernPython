def attack(person1, person2):
    person2['health'] = attack1(person1,person2)#person2['health'] - person1['damage']
    print(f"У игрока {person2['name']} отнялось {person1['damage']/person2['armor']} hp и составляет {person2['health']} здоровья")


def attack1(person1, person2):
    damage = person2['health'] - person1['damage'] / person2['armor']
    #print(f"У игрока {person2['name']} отнялось {person1['damage']} hp и составляет {person2['health']} здоровья")
    return damage

name_value = input('Введите имя игрока: ')
player = {'name': name_value, 'health': 100, 'damage': 60, 'armor': 2.0}
enemy = {'name': 'bot', 'health': 100, 'damage': 65, 'armor': 1.2}

attack(enemy, player)
print(player)
