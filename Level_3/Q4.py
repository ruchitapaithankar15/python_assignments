class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

if __name__ == "__main__":
    length = float(input("Enter the length of the square: "))
    square = Square(length)
    print(f"Area of the square: {square.area()}")
