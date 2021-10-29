n = int(input())
tickets_60, tickets_10, tickets_1 = 0, 0, 0
price_60 = price_10 = price_1 = 0
while n > 0:
    if n >= 60:

        price_60 = 440 * (n // 60)
        tickets_60 = n // 60

        n = n % 60

    if 60 > n >= 10:
        price_10 = 125 * (n // 10)
        tickets_10 = n // 10
        if price_10 < (tickets_10 +1)*125:
            tickets_10 = tickets_10 +1
            n = 0
        n = n % 10

    if n < 10:
        price_1 = 15 * (n // 1)
        tickets_1 = n

        n = n % 1
#if sum(price_1, price_10, price_60) >
print(tickets_1, tickets_10, tickets_60, price_1, price_10, price_60, price_1 + price_10 + price_60)


