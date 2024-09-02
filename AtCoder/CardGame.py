N = int(input(":"))
A = list(map(int, input(":").split()))
A.sort(reverse = True)
result = A[0]
for index, i in enumerate(A[1:]):
    if index % 2 != 0:
        result += i
    else:
        result -= i

print(result)