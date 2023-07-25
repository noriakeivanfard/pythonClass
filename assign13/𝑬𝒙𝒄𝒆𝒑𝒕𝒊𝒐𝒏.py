#name error
"""When you have a text value in a 
formula, it should be enclosed in 
double quotation marks. If it is not
Excel will try to interpret that 
value as either a named range or 
a function name. When neither 
works, it will return a #NAME error. """

try: 
    x == 2
except NameError as error:
    print("name x is not defined")
    
#SyntaxError
"""When the interpreter comes 
across an invalid syntax while
writing Python code, a 
SyntaxError is said to occur. 
Usually, the interpreter 
parses the Python code to 
convert it into bytecode and on 
encountering any invalid 
syntax in the parsing stage, 
 it throws an error called the 
SyntaxError"""

try:
    while True print('Hello')
except SyntaxError as error: 
    print("SyntaxError: invalid syntax")
    
#AttributeError
"""To avoid the AttributeError in 
Python code, a check should be 
performed before referencing an 
attribute on an object to ensure 
that it exists. The Python help() 
function can be used to find out 
all attributes and methods related
to the object."""

try:
    nooria_k
except AttributeError as error: 
    print("partially initialized module 'nooria_k'")
    
#TypeError
"""The Python TypeError is an 
exception that occurs when the
data type of an object in an 
operation is inappropriate. 
This can happen when an 
operation is performed on an 
object of an incorrect type, or
 it is not supported for the object."""
 
try:
    'nooria'+ 5
except TypeError as arror:
    print("can only concatenate str (not "int") to str")
