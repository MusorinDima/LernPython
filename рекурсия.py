c = 0
def F(n):
    global c
    #print('*')
    c += 1
    if n >= 1:
        #print('*')
        c += 1

        F(n - 1)
        F(n - 2)
        #print('*')
        c += 1

F(35)
print(c)