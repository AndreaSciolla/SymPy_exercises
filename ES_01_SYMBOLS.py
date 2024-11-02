"""
Author: Andrea Sciolla

Script Description:
This script demonstrates the use of the SymPy library to perform symbolic mathematics operations in Python. 
It defines symbolic variables and creates expressions involving powers and addition. 
The script then performs various algebraic manipulations, such as adding constants, combining terms, and expanding expressions.
"""



import sympy
from sympy import symbols

x, y = symbols("x, y")

# 2(x^2)+5 
expr = 2*(x**2) + 5

print(expr)
print(expr + 5) #2(x^2)+10

# 2(x^2)+y
expr_2 = 2*(x**2) + y
print(expr_2)
print(expr_2 + y) #2(x^2)+2y

expr_3 = 3*(x**2) + y
print(sympy.expand(expr_3 * y)) #3*x**2*y + y**2