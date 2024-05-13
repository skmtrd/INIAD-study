def repdigit(nums):
    result = []
    for num in nums:
        s_num = str(num)
        first = s_num[0]
        pre_result = []
        for i in s_num:
            if i != first:
                break
            else:
                pre_result.append(i)

        if len(pre_result) == len(s_num):
            result.append(num)

    return result

print(repdigit([345, 67, 1111111111, 0, 334]))
