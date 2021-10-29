import sys
from func_m import create_file, create_folder, get_list, delete_file, copy_file, save_info, smena_dir
from game_random import game

save_info('cтарт')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print(' Отсутсвует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название папки')
    else:
        create_folder(name)

elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название папки')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Введите название папки и название файла')
    else:
        copy_file(name, new_name)
elif command == 'change_dir':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название папки')
    else:
        smena_dir(name)

elif command == 'game':
    game()


elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
save_info('конец')