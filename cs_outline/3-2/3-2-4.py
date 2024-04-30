def same_number (x, y):
    result = []
    for num1 in x:
        for num2 in y:
            if num1 == num2:
                result.append(num2)
    return result

list1 = [1,100,80,7]
list2 = [1,90,7,800]
print(same_number(list1, list2))

#[1,7]




numbers = [1,2,3]
print(double(numbers))
print(double(numbers))