budget = int(input())
while budget >= 0:
    price = input()
    if price == 'End':
        print("You bought everything needed.")
        break
    budget -= int(price)
else:
    print("You went in overdraft!")