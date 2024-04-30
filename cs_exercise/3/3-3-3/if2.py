year = int(input("生まれた年を入力してください :"))
month = int(input("生まれた月を入力してください :"))
day = int(input("生まれた日を入力してください :"))
if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
    print("生年月日が間違っています")
else:
    if month == day:
        print("大吉")
    elif month % 2 == day % 2:
        print('中吉')
    elif month % 4 == day % 4:
        print("凶")
    else:
        print("吉")

