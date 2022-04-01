class Rectangle():
    length = 0
    width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def display(self):
        print(self.length, self.width, self.perimeter(), self.area())


rec = Rectangle(10, 5)
rec.display()


class Parallelepipede(Rectangle):
    high = 0

    def __init__(self, length, width, high):
        super().__init__(length, width)
        self.high = high

    def volume(self):
        print(self.length * self.width * self.high)

prl = Parallelepipede(10, 5, 6)
prl.volume()