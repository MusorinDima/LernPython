number_1 = float(input('Введите первое число: '))
simv = input('введите операцию (+,-,/,*,^): ')
number_2 = float(input('Введите второе число: '))


if simv == '+':
    print('Ответ: ', number_1 + number_2)

elif simv == '-':
    print('Ответ: ', number_1 - number_2)

elif simv == '/':
    print('Ответ: ', number_1 / number_2)
elif simv == '*':
    print('Ответ: ', number_1 * number_2)
elif simv == '^':
    print('Ответ: ', number_1 ** number_2)
else:
    print('Введена неверная операция')
