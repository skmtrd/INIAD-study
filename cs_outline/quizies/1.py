def count_cap(words):
    count = 0
    for word in words:
        if word[0].isupper():
            count += 1
    return count
in_list = ['Hello', 'world', 'I', 'am', 'a', 'Python', 'programmer']
print(count_cap(in_list))