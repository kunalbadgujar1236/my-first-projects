
### 1. Integer (`int`)

  #   #    # -**Properties:** 
     # -Represents whole numbers.
     # -Can be positive or negative.
     # -No size limit, constrained only by available memory.

 
a = 10
b = -5
c = 12345678901234567890

print(a)  # 10
print(b)  #    -5
print(c)  # 12345678901234567890
  

### 2. Floating   -Point (`float`)

  #   #   #    # -**Properties:** 
     # -Represents real numbers with a decimal point.
     # -Can represent very large or very small numbers using scientific notation.

 
x = 3.14
y =    -2.5
z = 1.2e3  # 1.2 * 10^3

print(x)  # 3.14
print(y)  #    -2.5
print(z)  # 1200.0
  

### 3. Complex (`complex`)

  #   #   #   #    # -**Properties:** 
     # -Represents complex numbers with a real and imaginary part.
     # -The imaginary part is denoted with a `j`.

 
c1 = 1 + 2j
c2 = 3    # -4j

print(c1)  # (1+2j)
print(c2)  # (3   -4j)
  

### 4. String (`str`)

  #   #   #   #    # -**Properties:** 
     # -Represents a sequence of characters.
     # -Immutable (cannot be changed after creation).
     # -Supports various operations like slicing, concatenation, and formatting.

 
s = "Hello, World!"
print(s)  # Hello, World!
print(s[0])  # H
print(s[7:12])  # World
print(s.upper())  # HELLO, WORLD!
  

### 5. List (`list`)

  #   #   #   #    # -**Properties:** 
     # -Ordered, mutable (can be changed after creation).
     # -Can contain elements of different types.
     # -Supports indexing, slicing, and various methods.

 
lst = [1, 2, 3, "a", "b", "c"]
print(lst)  # [1, 2, 3, 'a', 'b', 'c']
print(lst[0])  # 1
lst.append(4)
print(lst)  # [1, 2, 3, 'a', 'b', 'c', 4]
  

### 6. Tuple (`tuple`)

  #   #   #   #    # -**Properties:** 
     # -Ordered, immutable.
     # -Can contain elements of different types.
     # -Supports indexing and slicing.

 
t = (1, 2, 3, "a", "b", "c")
print(t)  # (1, 2, 3, 'a', 'b', 'c')
print(t[0])  # 1
print(t[1:4])  # (2, 3, 'a')
  

### 7. Dictionary (`dict`)

  #   #   #   #    # -**Properties:** 
     # -Unordered, mutable.
     # -Stores key   -value pairs.
     # -Keys must be unique and immutable (e.g., strings, numbers).

 
d = {"name": "Alice", "age": 30, "city": "New York"}
print(d)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(d["name"])  # Alice
d["age"] = 31
print(d)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}
  

### 8. Set (`set`)

  #   #   #   #    # -**Properties:** 
     # -Unordered, mutable.
     # -Does not allow duplicate elements.
     # -Supports set operations like union, intersection, and difference.

 
s = {1, 2, 3, 3, 4}
print(s)  # {1, 2, 3, 4} (duplicates removed)
s.add(5)
print(s)  # {1, 2, 3, 4, 5}
  

### 9. Boolean (`bool`)

  #   #   #   #    # -**Properties:** 
     # -Represents two values: `True` or `False`.
     # -Used in conditional statements and logical operations.

 
a = True
b = False
print(a)  # True
print(b)  # False
print(a and b)  # False
print(a or b)  # True
  

### 10. NoneType (`NoneType`)

  #   #   #   #    # -**Properties:** 
     # -Represents the absence of a value or a null value.
     # -Only one value: `None`.

 
n = None
print(n)  # None
print(n is None)  # True
  

### Summary

# Here is an example script demonstrating all these data types and their properties:

 
# Integer
a = 10
b =   -5
print("Integer:", a, b)

# Float
x = 3.14
y =   -2.5
print("Float:", x, y)

# Complex
c1 = 1 + 2j
c2 = 3   # # -4j
print("Complex:", c1, c2)

# String
s = "Hello, World!"
print("String:", s)
print("String slice:", s[0:5])

# List
lst = [1, 2, 3, "a", "b", "c"]
print("List:", lst)

# Tuple
t = (1, 2, 3, "a", "b", "c")
print("Tuple:", t)

# Dictionary
d = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", d)

# Set
s = {1, 2, 3, 3, 4}
print("Set:", s)

# Boolean
a = True
b = False
print("Boolean:", a, b)

# NoneType
n = None
print("NoneType:", n)
  

# This script shows how to create and use each of the main data types in Python.