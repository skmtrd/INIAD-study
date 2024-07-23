class Counter:
    def __init__(self, n):
        self.count = n

    def increment(self):
        self.count += 1
    
    def reset(self):
        self.count = 0



c1 = Counter(5)

for _ in range(3):
    c1.increment()
    print(c1.count)

c1.reset()
print(c1.count)