# Рассматривается множество целых чисел,
# принадлежащих отрезку [1030; 7730],
# которые делятся на 4 и не делятся на 12, 15, 17 и 21.
# Найдите количество таких чисел и максимальное из них.
# В ответе запишите два числа через пробел: сначала количество,
# затем максимальное число.
s = 0

for i in range(1030, 7731):
    if i % 21 != 0 and i % 17 != 0 and i % 15 != 0 and i % 12 != 0:
        if i % 4 == 0:

            s += 1


print(s)