class BodyShape:
    def __init__(self, h, w):
        self.height = h
        self.weight = w


    def is_taller_than(self, other):
        return self.height > other.height
    

taro = BodyShape(170.0, 60.0)
hanako = BodyShape(160.0, 50.0)
print(hanako.height)

print(taro.is_taller_than(hanako))
