fruits = ['apple', 'banana','pineapple', 'orange']
fruits2 = ['apple', 'banana','pineapple', 'kivi', 'mango']
# resultat =[]
# for i in fruits:
#     if i in fruits2:
#         resultat.append(i)
# print(resultat)

resultat = [i for i in fruits if i in fruits2]
print(resultat)
