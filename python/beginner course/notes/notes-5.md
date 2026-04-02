# Machine Learning

## Introduction

In this section, you are gonna learn about **Machine Learning**, which is the subset of **Artificial Intelligence**.

It is one of the trending topics in the world these days, and It gonna have a lot of applications in the future.

#### For Example:

Imagine I ask, you to write a program to scan an image, and tell me is it a cat or dog in the image.

If you gonna write a program on the traditional programming techniques, your program is gonna over complex.
You are gonnal look for lot of rules, you will look for curves, edges, and colors in an image. Just to identify is it a cat or dog.
And you just detected!

But,
- If I give you a Black & White picture of a same cat
- If I give you a picture of Cat or Dog from different Angle

Your rules may not work, and you have to rewrite them.

**So**, If you want to write that program based on ordinary programming technique, your program is gonna over complex, too difficult to handle, and may be impossible to work.

And this matter even worse, when in future, I ask you to write a program to detect horses also, along with cats and dogs. Once again you have to rewrite all these rules.

## Machine Learning:

**Machine Learning is a technique to solve these kinds of problems.**

You build a model or an engine, and give it blocks of data.

You give it thousands or tens of thousands of pictures of cats and dogs. Our model will then find and learn the patterns in the given data.

So, we can give it a new picture of a cat, that hasn't seen beforeAnd it will tell you, is it a Cat, or Dog, or a Horse at a *certain level of accuracy*.

The more input data we give to it, the more accurate our model is gonna be.

### Applications of Machine Learning

That was the very basic example. It has many other applications:
- Self Driving Cars
- Robotics
- Language Processing
- Vision Processing
- Forecasting Stock Market / Weather

## Machine Learning in Action

### Steps:

1. Import the data (usually comes in the form of `*.csv`, known as database, with a lot of data.)

2. Clean the Data (it involves the modification of duplicated, incomplete or wrong data.) (If data is in the form of text we have to convert it into numerical value.) (This step totally depends upon kind of data you're working on.)

3. Split data into Training/Test Sets (divide your data about 80% for training and 20% for testing) (testing is so important)

4. Creating a Model (Selecting an algorithm to analyze the data. they're so many machine learning algorithms out there (e.g. decision trees, neural networks, etc.) each algorithm has pros & cons in accuracy and performance. So the algorithm you choose depends upon the type of problem you want to solve and the type of data.) (Good News: "You don't have to explicitly program an algorithm.) (There are a lot of libraries out there, that mobile this algorithm.) (One of the most popular library is the one we are gonna learn in this tutorial.)

5. Train the Model (we feed our training data, our model than looks for the patterns in our data.)

6. Make Predictions (next we ask our model to make predictions.) (Back to the example of cats & dogs, Ask a model, "Is this a cat or dog?", and a model will make a prediction.) (prediction is not always accurate. It's very likely your predictions are inaccurate.)

7. Evaluate & Improve (We evaluate our prredictions, measure there accuracy, and get back to our model and either select a different algorithm for more accurate result for kind of problem we're trying to solve, OR finetune the parameters of our models, so each algorithm has parameters, we can modify to optimize the accuracy.)

These are the high level steps used for Machine Learning.

## Libraries:

Make sure you look at the popular Python libraries we use for Python Machine Learning Projects.

### Numpy

- Most Popular  (Very Very Popular infact)
- It provides a multi-dimensional Array

### Pandas

- Data Analysis Library
- It provides a concept called Data ______
- A Data ______ is a two dimensional data structure, similar to an excel spreadhseet.
- In a Data ______ we have rows & columns ad we can select data accordingly.
- Very popular in Machine Learning & Data Science Projects.

### MatPlotLib

- Two dimensional plotting library
- Used for creating blocks

### Sci-kit Learn

- One of the most popular Machine Learning Library
- It provides most common algorithms (e.g. decision trees, neural networks, etc.)

## Tools:

### Anaconda

- It includes everything you need
- It installs Jupyter, Numpy, and other popular libraries.