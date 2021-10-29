import math

def sqrt(list):
    result = [i**(1/2) if i > 0 else i for i in list]
    return result


old_list = [1, 23, 44, -22, 1, 3, -234, 55, 21, 12, 43]


result = sqrt(old_list)
print(len(old_list),old_list)
print(len(result),result)
