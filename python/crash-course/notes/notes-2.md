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
These are the options one can perofrm on points.

### How to do this?

We will start by defining a class using `class` keyword.Then, we will give our class a name.

```python
class Point:
```

We capitalize the first letter of each word in this. This method is known as **Pascal**.
In this case we only have a single word, but let suppose we have multiple words, then we will use PascalCase. e.g `class EmailClient`.
It is known as Pascal naming convention. It comes from the old Pascal language.

`classPoint:` colon is used to define a block in Python.

In this block, we are gonna define all the methods (functions) that belong to Point.