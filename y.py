def mikitani(yen):
    str_yen = str(yen);
    result = ''
    count = 0
    for i in range(len(str_yen)-1, -1, -1):
        count += 1
        if count % 3 == 0 and count != 0:
            result = "," + str_yen[i] + result
            continue
        result = str_yen[i] + result
    return result
print(mikitani(1234342425325425))