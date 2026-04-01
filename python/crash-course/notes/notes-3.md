# Constructors

We have learnt how to create a new type in [notes-2.md](notes-2.md) using classes.

```python
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()

point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)

point2 = Point()
point2.move()
point2.draw()
```

Now, there is a tiny **problem** in this implementation.

```python
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")
```

We can create a point object without x or y coordinates.

```python
point = Point()     # Before we set `point.x`, let's print(point.x)
print(point.x)
```

And this will give an Attribute Error.

It is impossible to create a point without x and y coordinates.

And this doesn't makes sense because point always has coordinates.