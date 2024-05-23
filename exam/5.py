def filt (nums):
    return [num for num in nums if len(str(num)) == 5]

print(filt([12, 345, 67890, 1234, 56789, 1, 0, 12345678]))
xs = filt([12, 345, 67890, 1234, 56789, 1, 0, 12345678])
print(xs)


