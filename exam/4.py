def change(words):
    return ["un" + word for word in words]


print(change(['important', 'do', 'known']))
xs = change(['real', 'natural', 'attended', 'pack'])
print(xs)