computer = "4456"
run = True
def hit(a, b):
    result = 0
    if a[0] == b[0]:
        result += 1
    if a[1] == b[1]:
        result += 1
    if a[2] == b[2]:
        result += 1
    if a[3] == b[3]:
        result += 1
    return result
def blow(a, b):
    result = 0
    for i in a:
        if i in b:
            result += 1
    return result

while run:
    yourNumber = str(input("Enter number"))
    if len(yourNumber) != 4:
        continue
    hits = hit(computer, yourNumber)
    blows = blow(computer, yourNumber)
    print(f"{hits}Hit, {blows}Blows")
    if hits == 4:
        run = False





        


    

