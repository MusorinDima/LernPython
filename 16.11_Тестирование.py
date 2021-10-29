from random import *
# n = 10
# ans = ''
# bal = 0
# opened = 0
# for i in range(n):
#     if bal == 0:
#         ans += 1
#         bal +=1
#         opened += 1
#     elif opened == n// 2:
#         ans += ')'
#         bal -= 1
#     else:
#         type_ = randint(0, 1)
#         if type_ == 0:
#             ans += '('
n, k = 2, 20
if k < 5 * n:
    a = list(range(1, k + 1))
    shuffle(a)
    a = a[:n]
else:
    added = set()
    a = []
    for i in range(n):
        x = randint(1, k)
        while x in added:
            x = randint(1, k)
        a.append(x)
        added.add(x)
    shuffle(a)
    print(*a)

