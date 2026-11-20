
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

total = 0

n = int(input("How many stocks do you want to buy? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        amount = stocks[name] * quantity
        total = total + amount
        print("Investment in", name, "=", amount)
    else:
        print("Stock not found!")

print("Total Investment =", total)
