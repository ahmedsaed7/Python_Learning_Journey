# Python Variables
# Variables are used to store values in a program. They are essentially labels that we can use to refer to a value later in the program.
# Declare a Variable ==>  Variable Identifier = Variable Value
name = "Ahmed"  # name is of type str
age = 17  # age is  of type int
isStudent = True  # isStudent is of type bool
age = 'seventeen' # age is of type str
countruy = """ Egypt """ # countruy is of type str 
print(type(countruy))

print("***************casting*****************")
# Casting in Python (Converting Data Types)
#  - Casting in Python refers to the process of converting one data type to another.
#  - This is often necessary when performing operations that require specific data types,
#  - or when you want to manipulate data in a particular way.
# Common Data Types and Casting ==> Python supports several fundamental data types, including:
#  1-Numeric: int, float, complex
#  2-Boolean: bool
#  3-String: str

# we have to type of casting in Python :-
#   a-Implicit Casting:
#      - Python often performs implicit type conversion when it's safe to do so.
#      - For example:-
x = 10   # Integer
y = 2.5  # Float
# When we add x and y, Python implicitly converts x to a float:
result = x + y  # Result is 12.5 (a float)
print(result)
print(type(result))

#   b-Explicit Casting:
#      - To explicitly convert one data type to another, you can use the following built-in functions:
#           1-int(): Converts a value to an integer.
#           2-float(): Converts a value to a floating-point number.
#           3-str(): Converts a value to a string.
#           4-bool(): Converts a value to a Boolean (True or False).
#      Examples:-
#           1-Converting a float to an integer
h = 3.14 # float
print(f"The value of h = {h} and the type is {type(h)}")
z = int(h)  
print(f"The value of z = {z} and the type is {type(z)}")

#           2-Converting a string to an integer
s = "10"
print(f"The value of s = {s} and the type is {type(s)}")
n = int(s)  
print(f"The value of n = {n} and the type is {type(n)}")
#           3-Converting an integer to a float
a = 5
print(f"The value of a = {a} and the type is {type(a)}")
b = float(a)
print(f"The value of b = {b} and the type is {type(b)}")  
#           4-Converting a number to a string
c = 123
print(f"The value of c = {c} and the type is {type(c)}")
d = str(c)  
print(f"The value of d = {d} and the type is {type(d)}")

# Note that:-
#  Data Loss: When converting from a larger data type to a smaller one (e.g., float to int), you might lose precision.
#  Invalid Conversions: Attempting to convert incompatible data types can raise exceptions. For example, converting a string like "hello" to an integer will raise a ValueError.
#  By understanding the basics of casting, you can write more flexible and robust Python code.

# Python Variable Naming Conventions
# Python has a set of rules for naming variables, which are known as the Python naming conventions.
# Q1- What is a Variable?
# Ans- A variable is like a container that stores a value. This value can be a number, text, or any other data type.
# Rules for Naming Variables:
# 1- Start with a Letter or Underscore:
#       - A variable name must begin with either a letter (A-Z, a-z) or an underscore (_).
#       - It cannot start with a number.
# 2- Use Alphanumeric Characters and Underscores:
#     - After the first character, you can use letters, numbers, or underscores.
#     - Avoid using special characters like $, %, or @.
# 3- Case Sensitivity:
#     - Python is case-sensitive, so myVariable and myvariable are different variables.
# 4- Avoid Python Keywords:
#     - Don't use reserved words like if, else, for, while, etc., as variable names.
# Example:-

# Good variable names:
first_name = "Alice"
last_name = "Johnson"
age = 30
is_student = True

# Bad variable names:
q = "Alice"
w = "Johnson"
e = 30
r = True

# Illegal variable names:
# 1- 2myvar = "John" (error message)
# 2- my-var = "John" (error message)
# 3- my var = "John" (error message)
 
# Note that:-   
# Snake Case ==> Each word is separated by an underscore character: my_variable_name = "John" 

# Assigning Multiple Values to Multiple Variables in Python:-
# Python allows you to assign multiple values to multiple variables in a single line, making your code more concise and readable.
# Basic Syntax:
# variable1, variable2, variable3 = value1, value2, value3
# Example:-
p, l, j = 10, 20, 30
# This assigns 10 to x , 20 to y , and 30 to z .
print(p)  # Output: 10
print(l)  # Output: 20
print(j)  # Output: 30

# Assigning the Same Value to Multiple Variables:
v = f = r = 5
# This assigns the value 5 to all three variables a, b, and c.
print(v) # Output: 5
print(f) # Output: 5
print(r) # Output: 5

# Unpacking Values from Lists or Tuples:
# You can unpack the elements of a list or tuple into multiple variables:
my_list = [1, 2, 3]
o, i, u = my_list
print(o)
print(i)
print(u)
# This will assign 1 to x, 2 to y, and 3 to z+

#Outputting Variables in Python
# The print() Function ==> Python's built-in print() function is the primary way to display values of variables and other expressions to the console.


x = 10
y = "Hello, World!"
print(x)  # Output: 10
print(y)  # Output: Hello, World!

# Printing Multiple Values:-
# You can print multiple values in a single print() statement
name2 = "ali"
age2 = 20
print("Name:", name2, "And The Age:", age2)

# Formatting Output:
# 1- Using the % operator:
name3 = "samma"
age3 = 15
print("Name: %s, Age: %d" % (name3, age3))

# 2- Using f-strings (Python 3.6+)
name4 = "may"
age4 = 16
print(f"Name: {name4}, Age: {age4}")


number1 = 5 
number2 = 10 
print("The sum of ", number1 ,"and" , number2 ," is ", number1+number2)

# You can control the formatting of output using the sep and end parameters of the print() function:
print("Hello", "World", sep="-", end="!\n")

x1 = "Python "
y1 = "is "
z1 = "awesome"
print(x1 + y1 + z1)


# Q2-what is the output of this code ?
# x = 5
# y = "Ahmed"
# print(x + y)  
# The answer is TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Global Variables in Python 
# Q3-What are Global Variables?
# Answer:- In Python, global variables are declared outside of any function and can be accessed from anywhere within the script.
# Declaring a Global Variable: global_variable = value
global_variable = 10
#Accessing a Global Variable:
def my_function():
    print(global_variable)  # Accessing the global variable
my_function()  # Output: 10

def modify_global_variable():
    global global_variable
    global_variable = 20

modify_global_variable()
print(global_variable) 


x = "Mohameed"
def myfunc():
  x = "Ahmed"
  print("name in function " + x)

myfunc()

print("name out function " + x)


