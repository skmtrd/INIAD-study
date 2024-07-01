class Room:
    def __init__(self, nm, ar):
        self.name = nm
        self.area = ar

    def compare(self, val):
        if self.area > val:
            return f"{self.name} > {val}"
        elif self.area < val:
            return f"{self.name} <= {val}"

living = Room("living", 30.0)
print(living.compare(30.5))