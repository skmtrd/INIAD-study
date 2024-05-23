#問1
for i in range(int(input("a =")), int(input("b =")) + 1):
    print(i)

#問2
def rep(s, n):
    return s * n

#問3
def allunder(nums, threshold):
    return len([num for num in nums if num < threshold]) == len(nums)

#問4
def change(words):
    return ["un" + word for word in words]

#問5
def filt (nums):
    return [num for num in nums if len(str(num)) == 5]

#問6
def count(words):
    return len([i for word in words for i in word if i == "e"])
