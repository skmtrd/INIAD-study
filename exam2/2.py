def cnta(lst):
    return len([i for i in lst if i[0] == "a"])

ans = cnta(['apple', 'pen', 'banana'])
print(ans)
print(cnta(['tree', 'blue', 'peach']))
print(cnta(['ant', 'active']))
print(cnta(['circle', 'arm', 'accept', 'habit', 'apple']))