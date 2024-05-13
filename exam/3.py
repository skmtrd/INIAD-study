# def allusnder(nums, threshold):
#     result = True
#     for num in nums:
#         if num >= threshold:
#             result = False
#             break
#     return result




def allunder(nums, threshold):
    return len([num for num in nums if num < threshold]) == len(nums)


print(allunder([1, 3, 2, 4, 5], 4))
print(allunder([1, 3, 2, 4, 5], 5))
print(allunder([1, 3, 2, 4, 5], 6))
if allunder([1, 3, 2, 4, 5], 3):
    print('yes')
else:
    print('no')