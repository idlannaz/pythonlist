# Python Basics: Tuples, Sets, and Dictionaries

## Overview

This repository contains a collection of Python code snippets that demonstrate basic operations on tuples, sets, and dictionaries. The code is organized into different sections, each highlighting a specific feature or operation related to these data structures.

## Code Breakdown

### Accessing Elements in a Tuple

```python
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0])  # Output: apple
print(fruits[3])  # Output: date
```

- **Description**: This code demonstrates how to access elements in a tuple by index.

### Tuple Unpacking

```python
num_tuple = (1, 2, 3, 4, 5)
a, b, *rest = num_tuple
print(a)     # Output: 1
print(b)     # Output: 2
print(rest)  # Output: [3, 4, 5]
```

- **Description**: This snippet showcases tuple unpacking, where the elements of a tuple are assigned to individual variables.

### Immutability of Tuples

```python
fruits[1] = "blueberry"
# the code above will raise an error because tuples are immutable
```

- **Description**: This code demonstrates that tuples are immutable, meaning their elements cannot be changed after creation.

### Adding Elements to a Set

```python
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
```

- **Description**: This snippet shows how to add an element to a set using the `add` method.

### Set Operations

```python
primary_colors = {"red", "green", "blue"}
intersection_set = colors & primary_colors  # Intersection
union_set = colors ^ primary_colors          # Symmetric Difference
difference_set = colors - primary_colors     # Difference
print(intersection_set)  # Output: {'red', 'green', 'blue'}
print(union_set)         # Output: {'purple', 'yellow'}
print(difference_set)    # Output: {'yellow', 'purple'}
```

- **Description**: This code performs basic set operations such as intersection, symmetric difference, and difference.

### Subsets and Supersets

```python
print({"green"}.issubset(primary_colors))   # Output: True
print({"orange"}.issuperset(primary_colors)) # Output: False
```

- **Description**: This snippet checks if a set is a subset or superset of another set.

### Accessing Dictionary Values

```python
dict = {"Alice": 25, "Bob": 27, "Charlie": 30, "Diana": 33}
print(dict["Bob"])  # Output: 27
```

- **Description**: This code shows how to access a value in a dictionary using a key.

### Modifying a Dictionary

```python
dict["Eve"] = 88
dict["Alice"] = 95
del dict["Charlie"]
print(dict)  # Output: {'Alice': 95, 'Bob': 27, 'Diana': 33, 'Eve': 88}
```

- **Description**: This snippet demonstrates how to add, modify, and delete key-value pairs in a dictionary.

### Iterating Over a Dictionary

```python
for name, grade in dict.items():
    print(f"Student: {name}, Grade: {grade}")
```

- **Description**: This code shows how to iterate over a dictionary's key-value pairs using a for loop.

## Conclusion

These code snippets provide a basic introduction to working with tuples, sets, and dictionaries in Python. They illustrate common operations and demonstrate the fundamental properties of these data structures.
