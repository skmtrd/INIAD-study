def mean(data):
    return sum(data) / len(data)
    
def variance(data):
    m = mean(data)
    return sum([(x - m) ** 2 for x in data]) / len(data)

data = [172.8, 156.9, 175.9, 156.1, 166.8, 161.9, 166.9, 176, 159.8, 164, 160.3, 153.5, 174.1, 172.2, 172.7, 166.7, 173.7, 158, 172.7, 155.9]
print(mean(data))
print(variance(data))