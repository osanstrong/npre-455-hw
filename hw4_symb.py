
import sympy as sp
from sympy import Symbol as Sym
from sympy import sinh, cosh

S = Sym("S")
PI = sp.pi
R = Sym("R")
D = Sym("D")
L = Sym("L")

B = Sym("B")
A = Sym("A")


ex1 = B - S / (4*PI*D)
ex0 = (A * sinh(R/L) + B*cosh(R/L))/(R*4) + (D/(2*R*R)) * ((B*R/L-A)*sinh(R/L) + (A*R/L - B)*cosh(R/L))

sol = sp.solve((ex1, ex0), (A, B))

print(f"A: {sp.simplify(sol[A])}")
print(f"B: {sp.simplify(sol[B])}")
