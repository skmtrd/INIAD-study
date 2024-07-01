class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def area(self):
        return self._width * self._height
    
r = Rectangle(10, 20)
print(r.area())  # 200
print(r._width)
print(r._height)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
p1 = Point(2.0, 3.0)
p2 = Point(5.0, 7.0)
print(p1.distance(p2))  