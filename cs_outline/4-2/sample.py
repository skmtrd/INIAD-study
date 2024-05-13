def rectangle(x, y):
    for i in range(y):
        print("#" * x)

rectangle(5, 3)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def overlap(list1, list2):
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    return result

print(overlap([1,2,3,4,5], [2,3,5,7,11]))
