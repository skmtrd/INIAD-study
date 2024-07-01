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