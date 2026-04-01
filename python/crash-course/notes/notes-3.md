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
point = Point()     # Before we set point.x, let's `print(point.x)`
print(point.x)
```

And this will give an Attribute Error.

It is impossible to create a point without x and y coordinates.

And this doesn't makes sense because point always has coordinates.

## Constructors:

To solve this problem, we use a **Constructors**.

A constructor is a function that gets called at the time of creating an object.

At line, we're creating an object `point`, we want to pass a value to this object.

```python
point = Point(10, 20)
```

With this line of code, we have a `point` object, with its x and y coordinates.

### How do we do this?

To do this, we have to add a special method (function) in a class (template for objects).

Look at the name of this function:

```python
def __init__(self):
```

init is a short for initialize, and it is a function or method that get's called when we create a new Point object.

Write after `self` you are gonna **add two extra parameters** `x` and `y`.

```python
def __init__(self, x, y):
```

In this body of this method we will read the values of `x` and `y`, and will use them to initialize our object.

To initilaize our object, we write the code like:

```python
def __init__(self, x, y):
    self.x = x
    self.y = y
```

**self:** It is a reference to the current object.

When we create a new object, `self` references that object in a memory, the same object you're using to reference the variable.

Eariler, we type: `point.x = 10`, but now we just enter a value as a parameter when creating an object.

## Program

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(10, 20)
print(point.x)
```

### Result:

```bash
cd python main.py

10
```

## Recap:

1. Using this `__init__(self)` method we can initialize our object.
2. This `__init__(self)` method is known as constructor.
3. It is used to construct an object.