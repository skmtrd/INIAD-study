year = 0
debt = 100
finish = 200
APR = float(input("年利を入力してください:")) * 0.01

x = True

while x:

    debt += debt * APR
    year += 1
    if debt >= finish:
        x = False

print(year, "年です")