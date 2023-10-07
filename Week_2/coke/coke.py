amount_due = 50

while amount_due > 50:
    print("Amount Due: ", amount_due)

    insert_coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        amount_due -= insert_coin
        print(amount_due)

    