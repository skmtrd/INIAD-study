def picture_art(data):
    new_data = data.copy()
    for i in range(len(new_data)):
        for j in range(len(new_data[i])):
            if new_data[i][j] % 2 == 1:
                new_data[i][j] = "*"
            else:
                new_data[i][j] = " "
    for i in new_data:
        print("".join(i))

    
picture_art([[1,2,3],
            [3,3,3],
            [5,2,5]]) 