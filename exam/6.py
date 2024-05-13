def count(words):
    return len([i for word in words for i in word if i == "e"])

print(count(['enemies', 'enter', 'from', 'east']))
xs = count(['pineapple', 'banana', 'orange'])
print(xs)
