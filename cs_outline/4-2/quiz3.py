def my_string(s):
    result = ""
    for index, i in enumerate(s):
        if (index + 1) % 5 == 0:
            result += i
    return result

print(my_string('INIAD, Toyo University'))
        