def gt10(xs):
    return sum([x for x in xs if x >= 10])

ans = gt10([3, 19, 11])
print(ans)
print(gt10([15, 7, 6, 21]))
print(gt10([7, 11, 32]))
print(gt10([16, 24, 22]))
