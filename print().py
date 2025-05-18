
### 1. Basic Usage
#The `print()` function shows text or variables on the screen.
print("Hello, World!")
'''
Output:
Hello, World!
'''

### 2. Multiple Arguments
#The `print()` function can show several pieces of information at once, separated by a space.

name = "Alice"
age = 30
print("Name:", name, "Age:", age)
'''
Output:
Name: Alice Age: 30
'''

### 3. The `sep` Parameter
#The `sep` parameter changes the separator between different pieces of information. The default separator is a space.
print("apple", "banana", "cherry", sep=", ")
'''
Output:
apple, banana, cherry
'''

### 4. The `end` Parameter
#The `end` parameter changes what is printed at the end. The default is a new line.


print("Hello", end=" ")
print("World")

'''
Output:
Hello World
'''

### 5. The `file` Parameter
#The `file` parameter lets you print to a file instead of the screen.

with open("output.txt", "w") as file:
    print("Hello, file!", file=file)

#This writes "Hello, file!" to a file named `output.txt`.


### 6. The `flush` Parameter
#The `flush` parameter, when set to `True`, forces the print output to be written immediately.

import time

print("Loading...", end="", flush=True)
time.sleep(2)
print("Done")

'''
Output:
Loading...Done
'''

### 7. Formatted String Literals (f-strings)
#From Python 3.6, you can use f-strings to format output.

name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")
'''
Output:
Name: Alice, Age: 30
'''

### 8. Printing Special Characters
#You can print special characters using backslashes.

print("Hello\nWorld")
print("Hello\tWorld")
print("He said, \"It's a beautiful day!\"")
'''
Output:
Hello
World
Hello   World
He said, "It's a beautiful day!"
'''

### 9. Combining Strings and Variables
#You can mix strings and variables in the `print()` function.

name = "Alice"
print("Hello, " + name + "!")
'''
Output:
Hello, Alice!
'''

### 10. Printing Data Structures
#You can print lists, dictionaries, and tuples directly.

my_list = [1, 2, 3]
my_dict = {"name": "Alice", "age": 30}
print("List:", my_list)
print("Dictionary:", my_dict)
'''
Output:
List: [1, 2, 3]
Dictionary: {'name': 'Alice', 'age': 30}
'''

### Example Program Demonstrating All Properties

name = "Alice"
age = 30
fruits = ["apple", "banana", "cherry"]
details = {"name": name, "age": age}

# Basic usage
print("Hello, World!")

# Multiple arguments
print("Name:", name, "Age:", age)

# sep parameter
print("apple", "banana", "cherry", sep=", ")

# end parameter
print("Hello", end=" ")
print("World")

# file parameter
with open("output.txt", "w") as file:
    print("Hello, file!", file=file)

# flush parameter
import time
print("Loading...", end="", flush=True)
time.sleep(2)
print("Done")

# Formatted string literals (f-strings)
print(f"Name: {name}, Age: {age}")

# Special characters
print("Hello\nWorld")
print("Hello\tWorld")
print("He said, \"It's a beautiful day!\"")

# Combining strings and variables
print("Hello, " + name + "!")

# Printing data structures
print("List:", fruits)
print("Dictionary:", details)