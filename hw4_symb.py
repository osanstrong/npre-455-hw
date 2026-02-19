
import sympy as sp
from sympy import Symbol as Sym
from sympy import sinh, cosh

S = Sym("S")
PI = sp.pi
# R = Sym("R")
# D = Sym("D")
# L = Sym("L")

# B = Sym("B")
# A = Sym("A")


# ex1 = B - S / (4*PI*D)
# ex0 = (A * sinh(R/L) + B*cosh(R/L))/(R*4) + (D/(2*R*R)) * ((B*R/L-A)*sinh(R/L) + (A*R/L - B)*cosh(R/L))

# sol = sp.solve((ex1, ex0), (A, B))

# print(f"A: {sp.simplify(sol[A])}")
# print(f"B: {sp.simplify(sol[B])}")

A1 = Sym("A1")
A2 = Sym("A2")
B1 = Sym("B1")
B2 = Sym("B2")

D1 = Sym("D1")
L1 = Sym("L1")
D2 = Sym("D2")
L2 = Sym("L2")


at = Sym("at")
bt = Sym("bt")

ex2 = at + B1
ex3 = bt - B2
ex4 = (D2*A2/L2) * cosh(B2/L2) - (D1*A1/L1) * cosh(B1/L1) - S
ex5 = A1*sinh(B1/L1) - A2*sinh(B2/L2)

sol2 = sp.solve((ex2, ex3, ex4, ex5), (A1, A2, B1, B2), dict=True)[0]

print(f"A1: {sp.simplify(sol2[A1])}")
print(f"B1: {sp.simplify(sol2[B1])}")
print(f"A2: {sp.simplify(sol2[A2])}")
print(f"B2: {sp.simplify(sol2[B2])}")