def ex100(nums):
    for num in nums:
        if num == 100:
            return "OK"
    return "NG"


ans = ex100([75, 80, 100, 95])
print(ans)
print(ex100([15, 60, 80, 55]))
print(ex100([55, 35, 70, 58]))
print(ex100([100, 100, 100, 100]))
print(ex100([98, 100, 100, 100]))
print(ex100([100, 90, 95, 100]))