# Classes

class Point:            # we use classes to define new types.
    def move(self):     # these types can have methods that we define
        print("move")
    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10           # they can also have attributes we can set anywhere in a program
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)         # this gives an error, if point2.x is not defined