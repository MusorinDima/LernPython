import random


def game():
    number = random.randint(1, 100)
    # user_number = None
    count = 0
    levels = {1: 10, 2: 5,
              3: 3}  # 1.игроку не понятно какие уровни существуют 2. нет обработки неверно заданного уровня
    level_keys = list(levels.keys())
    while True:
        level = int(input(f"Выберите уровень сложности {min(level_keys)} - {max(level_keys)}: "))
        if level not in level_keys:
            print("Введен неверный уровень сложности")
            continue
        else:
            break
    max_count = levels[level]
    user_count = int(input("Введите кол-во игроков: "))
    users = []
    for i in range(1, user_count + 1):
        user_name = input(f"Введите имя игрока №{i}:")
        users.append(user_name)
    print(users)
    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print("Вcе игроки проиграли")
            break
        print(f"Попытка №{count}")
        for user in users:
            print(f"Ход игрока {user}")

            user_number = int(input("Введи число: "))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print(f"Число {user_number} больше загаданного")
            else:
                print(f"Число {user_number} меньше загаданного")
    else:
        print("Ты угадал число!")
        print(f"Победитель {winner_name}")
