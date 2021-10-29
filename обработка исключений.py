# is_has_name = False
# name = 'Max' if is_has_name else 'Empty'
# print(name)
#
# is_one = True
# number = 1 if is_one else 2
# print(number)
#

word = 'Привет'
result = []
for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i % 2 != 0 else letter.upper()
    result.append(letter)

result = ''.join(result)
print(result)
