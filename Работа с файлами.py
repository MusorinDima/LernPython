a = open('first.txt', 'r')
# a.write('Hello\n')
# a.write('Dima\n')
# a.writelines(['Ky\n', 'Dima\n'])
for line in a:
    print(line.replace('\n', ''))
a.close()
with open('first.txt', 'r') as a:
    for line in a:
        print(line.replace('\n', ''))
print('end')
