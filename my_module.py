# Создайте модуль
# (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле
import os


def create_dir(path, qty):
    papki = 'dir_'
    new_path = os.path.join(path,papki)
    for i in range(1, qty+1):

        os.mkdir(new_path + str(i) )

# ff = '/home/damintik'
# create_dir(ff,10)
def delete_dir(path, qty):
    papki = 'dir_'
    new_path = os.path.join(path, papki)
    for i in range(1, qty + 1):
        os.rmdir(new_path + str(i))

#delete()

