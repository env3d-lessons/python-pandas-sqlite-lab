# python-pandas-sqlite-exercise

Review the lesson at https://github.com/env3d/python-pandas-sqlite-basics 

Put all your functions in a file called **`main.py`**

Use the `title.basic.tsv` dataset, create a python function that calculates the average runtime of a particular 
titleType for a particular year:

```python
>>> import main
>>> main.calculate_average_runtime('short', 2000)
14.843252950230887
>>> main.calculate_average_runtime('movie', 2022)
92.60836196184489
>>>
```

You will use the 2 techniques covered in the above lesson.  The resulting function only has a few lines of code, 
but will require you to take care of various data cleaning issues such as converting \N to NaN.

For the first version, you will develop your function using pandas dataframe with chunks, the function signature 
is as follows:

```
def calculate_average_runtime( titleType, year):
```
 
For the second version, you will develop 2 functions, first function will read the data file into a database, and 
the second function will perform the calculation:

```
def write_to_database():
```

```
def calculate_average_runtime_db( titleType, year):
```

