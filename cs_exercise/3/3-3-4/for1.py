num = int(input("数字を入力してください :"))
s = 0
for i in range(num + 1):
    if i == 0:
        continue
    s += 1 / (i**2)
result = (6 * s) ** 0.5
print(result)