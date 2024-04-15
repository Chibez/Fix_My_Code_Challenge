#!/usr/bin/python3

class Square:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
