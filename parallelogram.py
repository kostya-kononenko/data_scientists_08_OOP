class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return 2*((self.width)**2 + (self.length)**2)


a = Parallelogram(4, 5)
print(a.get_area())


class Square(Parallelogram):
    def __init__(self, width, length):
        super().__init__(width, length)

    def get_area(self):
        if self.width == self.length:
            return self.width * self.length
        else:
            return 'У квадрата не можуть бути різні сторони'


b = Square(5, 5)
print(b.get_area())
