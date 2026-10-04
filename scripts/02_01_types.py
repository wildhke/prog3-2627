# %% [markdown]
# ### Single data types (Numbers, Strings, Bytes, Booleans)
# We want to store information (mainly numbers) in memory to access it for
# further processing. So that it makes sense to better understand the
# underlying structure.
#
# In Python, we:
# - Use variable without declaring them (lazy developers)
# - Associativity : Left to right
# - Call by object reference (neither call by reference, nor call by value in general)
# - Do not have to deal with dereference etc. (compare to C++)
# - Use existing modules which are robust and well tested (prominent ones)

# %% [markdown]
# #### Numbers (the most important basics)

# %%
# Integer
a = 1
b = 0x10
print(type(b))

# Floating point
c = 1.0
d = 5e-10
e = 0.5
print(type(e))

# Complex
f = 2 + 1j
g = complex(1, 2)
print(type(g))

# %% [markdown]
# #### Strings (pathes, were to find the data, descibe something, for instance label of axis, ...)

# %%
h = "Hello world"
print(type(h))
raw_string = r"/usr//bin/bash"

# %% [markdown]
# #### Boolean to simply store binary information (passed, failed, exists, flag, ...)

# %%
i = True
print(type(i))

# %% [markdown]
# #### Byte (often used while reading data)

# %%
j = b"a"  # a --> Bin=1100001 Dec=97
print(type(j))
print((j[0]))

# %% [markdown]
# #### NoneType

# %%
k = None
print(type(k))

# %% [markdown]
# ### Structured data types (Lists, Tuples, Sets, Dicts)

# %% [markdown]
# #### Lists and tuples (very often used to store sequences and time series)
# Store multiple numbers within one data sequence.
# Lists are in the form of:  x ∈ N^(n x 1)

# %%
l = [1, "2", str(3), 4 + 1j, 55e-10]  # in python you can mix data types
#    0,  1 ,   2   ,   3  ,    4
print(type(l))

# Length of a list (elements within the brackets)
print(len(l))
# Slicing (go to specific elements within list)
print(l[0])  # very first element in list
print(l[-1])  # last element in list
print(l[1:4])

# Appending elements to list
l.append("sixth")
# Appending list to list
l.extend([7, 8])

# Remove values
l.pop()  # Pop last element
l.pop(2)  # Pop third element
l.remove("sixth")  # Remove element by key
del l[0]

# Get index of specific value
l.index((5.5e-09))
print(l.index((5.5e-09)))

# %% [markdown]
# #### Tuple

# %%
m = (1, 2, 3, 4, [5, 6])
print(type(m))

# %% [markdown]
# #### Multidimensional lists
# Lists consists of Lists are also existing. Often used to store object data
# such as images and other n-dim data. The form of list of lists is defined as
# the following:  x ∈ N^(n x m)

# %%
rows = [[128, 102, 256], [102, 148, 124], [24, 78, 154], [24, 78, 154]]

# %%
## Set https://docs.python.org/3/tutorial/datastructures.html#sets
n = set(["This", "is", "a", "set"])
print(n)
n.add("T")  # Add items
print(n)
n.add("T")  # Duplicate not allowed
print(n)
n.discard("T")  # Discard item
n.remove("This")  # Remove item
print(n)
print(n.pop())  # in a notebook the popped value is shown automatically

# %%
## Dict
o = {"key": "value"}  # {key: value}
o["key_2"] = "value_2"
print(o)

# %% [markdown]
# ## In-build functions, unary and binary operators
# If you want to multiply simple numbers, want to determine the difference or
# you want to check if a number is even or odd, you have to use simple
# mathematical operations. Fundamental operations are included in plain
# python. If you need more mathematical funtions, we recommend numpy:
# https://numpy.org/doc/stable/user/whatisnumpy.html

# %% [markdown]
# #### unary and binary operators

# %%
# Addition
print("---- Addition ----")
print(1 + 1)
print("------------------")
print("\n")

# Concatenate lists
print("---- Concat ----")
print([1, 2, 3] + [4, 5, 6])
print("----------------")
print("\n")

# Subtraction
print("---- Subtraction ----")
print(10 - 6)
print("---------------------")
print("\n")

# Multiplication
print("---- Multiplication ----")
print(10 * 0.45)
print("------------------------")
print("\n")

# Division (float)
print("---- Division (float) ----")
print(10 / 2)
print("--------------------------")
print("\n")

# Division (int)
print("---- Division (int) ----")
print(10 // 2)
print("------------------------")
print("\n")

# Power of 2
print("---- Power ----")
print(10.0**2)
print("----------------")
print("\n")

# Modulo
print("---- Modulo (Divison with rest) ----")
print(10.1 % 2)
print("------------------------------------")
print("\n")

# Bitshift
print("---- Bitshift (Multiplication by 2) ----")
print(128 * 2)
print("Bitshift, one position, left")
print(128 << 1)
print("\n")
print(256 // 2)
print("Bitshift, one position, right")
print(256 >> 1)
print("------------------------------------")
print("\n")

# %% [markdown]
# #### Casts (cast one data type to another -> Print a string obtained from int)

# %%
# Cast integer (2) to an string, called string
string = str(2)

# Cast string '2' to float
number = float("2")

# Cast list of numbers to tuple
casted_list = tuple([1, 2.0, 3, 5])

# All day example:
string = str(42)
print("Meaning of life: " + string)

# %%
# Display casted data type
print(type(casted_list))

# %% [markdown]
# ## Modules & Functions

# %% [markdown]
# ### Modules, standard libraries
# (In a script, imports belong at the top of the file - see above.
#  They are repeated here only to show the syntax.)

# %%
# Import library X
import sys

print(sys.version)  # Which version of python do I have installed?

# Import library X as Y (instance)
import numpy as np

print(np.zeros(10, dtype=int))

# %% [markdown]
# ### Functions
# A function is a (user-) defined block of code which only runs when it is
# called (so-called function-call). You can pass every kind of data
# (parameters) into a function. A function can either return data as a result
# or work on "reference".

# %%
## Functions of modules
deg = np.sin(90)

# Calling a function within a function
rad = np.sin(np.deg2rad(90))  # Sinus of 90 deg * 180/pi = 90 rad

print("Answer in deg: " + str(deg) + "\n")
print("Answer in rad: " + str(rad))


# %%
def my_mean(input_argument):
    """
    Function to determine mean value
    :param inpute_argument: Input signal
    :type input_parameter: array like
    """
    sum = 0
    for i, _ in enumerate(input_argument):
        sum += input_argument[i]
    return sum / len(input_argument)


# %%
# Define list to determine the mean value of it. From 0 to 1000, step size = 1
my_list = np.arange(0, 1000, 1)

# %% [markdown]
# #### Example: Call by object reference

# %%
# Example 1: Parse list to function, multiply the first element and go back to main
test_int = [1.0, 1.0]
print("Original: " + str(test_int))


def change_my_int(x):
    """
    Function to multiply the first element of x with 42
    :param x: Input list
    :type x: list
    :return: None
    :rtype: None
    """
    x[0] = x[0] * 42


# Call function and hand over test_int
change_my_int(test_int)
# Print result
print("Processed: " + str(test_int))

# %%
# Example 2: Parse string to function, replace  "am" with "am not"
test_str = "I am Original"
print("Original: " + test_str)


def change_my_str(x):
    x.replace("am", "am not")


change_my_str(test_str)
print("Processed: " + test_str)

# %%
print("------- Validation -------")
print("Original: " + test_str)
print("Processed: " + test_str.replace("am", "am not"))

# %% [markdown]
# ## Comprehensions

# %% [markdown]
# #### Data set

# %%
# list with numbers
data = [1, 2, 3, 4]

# Dict with two fields, consists of strings, floats, Nones
data_set = {
    "Gender": ["m", "m", "m", "f", "f", "f", "d"],
    "Height": [1.85, 1.99, 1.87, 1.72, 1.68, None, 1.98],
}

# %% [markdown]
# #### If else

# %%
# Simple if-else, checking of data types
if isinstance(data, list):
    print("yes, it`s a list")
else:
    print("no, it`s not  list")

# If elseif else
if isinstance(data, tuple):
    print("it`s a tuple")
elif isinstance(data, list):
    print("it`s a list")
else:
    print("neither list, nor tuple")

# Check if numbers are equal
i = 1
if i == 1:
    print("i equals to 1")
else:
    print("i equals not to 1")

# Other comparisons avaiable

# != not
# < smaller than
# <= smaller equals
# > greater
# >= greater equals

# %% [markdown]
# #### try except (catch)
# To avoid unexpected behavior and to robusten your code, you can use
# try except/catch statements.
# Image: https://i.redd.it/atf1ietqwaxy.jpg

# %%
try:
    print(abc)
except NameError:
    print("Meme is not defined")
except:
    print("Something else went wrong")

# %% [markdown]
# ## Loops
# If you want to step through a data set or iterate over an array (for
# example, a specific image), you can use loops. However, use loops with
# caution because they are computationally intensive.
# Image: http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1508331558/Loop_2-2_igl4qt.jpg

# %% [markdown]
# #### while loop
# The loop consists of three components that you need to construct the
# *while* loop in Python:
#
# - The *while* keyword
# - A *condition* that transates to either True or False
# - A block of *code* that you want to execute repeatedly

# %%
# Running variable i
i = 0
while i < 20:  # Condition check, if True, go into code block
    print(i)
    # Dont forget to increment, otherwise you have a infinity loop
    i += 1  # Short for i = i + 1 (post-increment)

# %%
# Infinity loop
# Commented out: in a plain script this would never finish, so nothing below
# it would ever run. Uncomment to try it, and stop it with Ctrl+C.
#
# while 0.01:  # Every boolean (everything except 0 is true! )
#     print("I'll run till infinity")

# %% [markdown]
# #### for loop
# The loop consists of five elements that you need to construct the while
# loop in Python:
#
# - The *for* keyword
# - A running variable *i*
# - The *in* keyword
# - The *range()* function, which is an built-in function in the Python
#   library to create a sequence of numbers
# - The *code* that you want to execute repeatedly

# %%
# Easy for loop
# Running variable i (or k/j) is incremented after going into loop body.
# Running from 0 to 10 (exclude, 10 times in total)
for i in range(0, 10):
    print(i)

# %%
# You can use the length of a list to iterate over
for i in range(0, len(data)):
    print(data[i])

# %%
# Using itertors are more performant (at least in C/C++)
for index, value in enumerate([10, 20, 30, 40, 50, 60]):
    print("Index: " + str(index))
    print("Value: " + str(value))

# %%
# Using the for loop in one-liner
a = [x**2 for x in range(100)]
print(a)

# %%
