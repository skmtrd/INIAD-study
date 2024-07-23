class Mac:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def show (self):
        print(f"{self.name}は{self.value}円です")
    
    def discount (self, value):
        self.value -= value

L_potato = Mac("Large-potato", 380)
M_potato = Mac("Midium-potato", 200)


L_potato.discount(100)
L_potato.show()
