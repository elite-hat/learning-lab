# Real World Problem

## Problem

**Scenario:** Imagine we have an online music store. When the user signs in, you ask for there age and gender, and based on there profile, you recommend various music albums.

In this project we are gonna use Machine Learning Techniques.

We will build a model, and train it on the data based on the existing users. Our model will learn the patterns in our data. So, we can askit for predictions.

When the user sign ups, we tel our model "hey, look at this profile, what kinf of music he is interested in?"
Our Model will say: "Jazz, or HipHop, etc."

Based on that, we can make suggestions to our user.

This is the problem, we are gonna solve.

## Problem Solving

Back to our list of steps.

First we will import our data.

We have a file music.csv

```python
import pandas as pd
music_data = pd.read_csv("music.csv")
X = music_data.drop(columns=["genre"])
y = music_data["genre"]
```

We have imported the data and cleaned it, now we have to create a model.

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
music_data = pd.read_csv("music.csv")
X = music_data.drop(columns=["genre"])
y = music_data["genre"]

model = DecisionTreeClassifier()
model.fit(X,y)
```

We have import a class DecisionTreeClassifier, created a model, and trained it.

Now we are gonna test it.

```python
predictions = model.predict([ [21, 1], [22, 0] ])
```

Output: array(['HipHop', 'Dance'], dtype=object)

It is amazing our model is running correctly.

BUT! That is not how testing works.

We are gonna split the input and output databases from 2 to 4.

1. Input Training
2. Input Testing
3. Output Training
4. Output Testing





