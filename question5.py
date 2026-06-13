class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area =", area)

c = Circle(7)

c.area()
