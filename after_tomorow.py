d,m,y = input().split()
td = int(d) + 2
if td > 26:
    if int(m) == 2:
        if y % 4 ==0 and y % 100 !=0 or y % 400 ==0:
            if d == 27:
                td = 29
            elif d == 28:
                td = 1
                m = m + 1
            elif d == 29:
                td = 2
                m = m + 1
            else:
                print("Wrong date", d,m,y)
        else:
            if d == 27:
                td = 1
                m = m + 1
            elif d == 28:
                td = 2
                m = m + 1
            else:
                print("Wrong date",d,m,y)





print(td,m,y)