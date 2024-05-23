def count_char(line, c):
    result = 0
    for i in line :
        if i == c :
             result += 1
    return result

print(count_char("ざわわざわわ", "わ"))