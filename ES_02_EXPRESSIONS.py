"""
Author: Andrea Sciolla

Script Description: 
"""

import sympy
from sympy import symbols, pretty_print, solve, expand, factor, simplify

x, y, z = symbols("x y z")

expr = 2*x + 5
expr2 = x**2 - x -6
expr3 = x**2 + y**2
expr4 = (x - 6)/(y + 5)
expr5 = (x + 1)*(x + 5)*(x - 6)

print(expr2.subs(x, -2)) 

print(expr3.subs([(x, 2), (y, 3)]))
print(expr3.subs({x: 2, y: 3})) #same with a dictionary

print(expand(expr5))  # x**3 - 31*x - 30
expr6 = x**3 - 31*x - 30
print(factor(expr6)) # (x + 1)*(x + 5)*(x - 6)

expr7 = x*(y + 5)
print(expand(expr7)) #x*y + 5*x
expr8 = x*y + 5*x
print(simplify(expr8))