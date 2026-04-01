# CLASSES in python

## Data Types:

### Simple
1. Numbers
2. Strings
3. Booleans
   
### Complex
1. Lists
1. Dictionaries
   
---
   
### Note:

They are useful but not always capable to handle complex modern tasks.

* **Shopping Cart:** It's not any of the above

* **Point:** It's also not any of the above

We can use classes to define new types to model real concepts

---

## Creating a Class: `Point`

Here's how to define a new type called **Point**:

It gonna have methods to working with points.

### Introduction:

First let's have an introduction of Classes.

Suppose there is a list `numbers = [1, 2, 3]`. **List** is a specific data type.

When we type `.` after list name we get multiple methods i.e. `append()` or `clear()` etc.

Now similar to this we are gonna create a new type: **Point**

It gonna have methods like `move()`, `draw()`, `get_distance()`, etc.
These are the options one can perform on points.

### How to do this?

We will start by defining a class using `class` keyword.Then, we will give our class a name.

```python
class Point:
```

We capitalize the first letter of each word in this. This method is known as **Pascal**.
In this case we only have a single word, but let suppose we have multiple words, then we will use PascalCase. e.g `class EmailClient`.
It is known as Pascal naming convention. It comes from the old Pascal language.

`class Point:` colon is used to define a block in Python.

In this block, we are gonna define all the methods (functions) that belong to Point.

```python
class Point:
    def move(self)
```

As soon as we type `(` open parentheses in PyCharm, `self` is automatically written in ().

**self:** This is a special keyword. We will talk about it shortly.

In this method let's `print(move)` on the terminal.

```python
class Point:
    def move(self):
        print("move")
```

Now let's define another method `draw()`:

```python
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")
```

Now we are done with our Point class.

We need to add two line breaks.

**Recap**: In this Class we defined a new type, in this type, we defined two methods `move`, and `draw`.

## Usage of Class: `Point`

Within this new type (`Point`) we can create new objects.

**Object:** It is a new instance of class.

A class simply defines a blueprint or template for creating templates.
While objects are the actual instances based on that template.

So we could have tens of hundreds of points on the screen using tens of hundreds of objects of that class.
All of these (tens of hundreds of) objects will have methods we define in class template