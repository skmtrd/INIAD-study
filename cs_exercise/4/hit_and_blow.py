computer = "4567"

def hit (a, b):
    result = 0
    for i in range(4):
        if a[i] == b[i]:
            result += 1
    return result

def blow (a, b):
    result = 0
    for i in range(4):
        for j in range(4):
            if a[i] == b[j]:
                result += 1
    return result - hit(a, b)

run = True

while run :
    yourNumber = str(input("Enter number: "))
    if len(yourNumber) != 4:
        continue
    hits = hit(computer, yourNumber)
    blows = blow(computer, yourNumber)
    if hits == 4:
        run = False
        break
    print(f"{hits}Hit, {blows}Blows")

print("Correct!")
   