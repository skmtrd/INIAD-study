map = [[0,0,0],
       [0,0,0],
       [0,0,0]]

def printMap(map):
    for row in map:
        letter = ""
        for cell in row:
            letter += str(cell) + " "
        print(letter)

printMap(map)
run = True
turn = 1
while run :
    posX = int(input("x = "))
    posY = int(input("y = "))

    if 1 <= posX <= 3 and 1 <= posY <= 3:
        map[posY - 1][posX -1] = turn % 2
        printMap(map) 
        turn += 1
    else:
        print("one more")
