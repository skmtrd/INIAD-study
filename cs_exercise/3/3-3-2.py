run = True
count = 0
subtotal = 0
while run:
    count += 1
    value = input(f"{count}個目の商品の価格(円)を入力してください:")
    if value == "q":
        run = False
        break
    subtotal += int(value)

tax = int(subtotal * 0.1)
total = subtotal + tax
print(f'小計:{subtotal}')
print(f'消費税:{tax}')
print(f':合計{total}')