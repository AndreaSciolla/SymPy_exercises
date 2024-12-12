from sympy import diff, symbols, cos, sin

x, y = symbols("x y")
expr1 = 2*x + 5
expr2 = x**3
expr3 = (x**2)*(y**2)
expr4 = x**4 + 3*x**2 + 9*x + 7
expr5 = cos(x)
expr6 = sin(y)
expr7 = sin(x)*cos(y)


print(diff(expr2, x)) #derivata prima
print(diff(expr3, x, 2)) #derivata seconda
print(diff(expr3, x, y)) #derivata sia per x che y
