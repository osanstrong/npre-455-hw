import sympy as sp
from sympy import Symbol as Sym
from sympy import sinh, cosh

S = Sym("S")
PI = sp.pi

A1 = Sym("A1")
A2 = Sym("A2")
B1 = Sym("B1")
B2 = Sym("B2")

D = Sym("D")
S = Sym("S")
L = Sym("L")
X_a = Sym("X_a")
X_ap = Sym("X_ap")

a = Sym("a")
at = Sym("at")
b = Sym("b")
c = Sym("c")

ex1 = A1*sinh(-2*D/L) + B1*cosh(-2*D/L) + S/X_a
ex2 = A2*sinh(at/L) + B2*cosh(at/L) + S/X_a
ex3 = (A1-A2)*sinh(c/L) + (B1-B2)*cosh(c/L)
ex4 = (D/L)*((A2-A1)*cosh(c/L) + (B2-B1)*sinh(c/L)) - b*X_ap*(A1*sinh(c/L) + B1*sinh(c/L) + S/X_a)

sol = sp.solve((ex1, ex2, ex3, ex4), (A1, A2, B1, B2), dict=True)[0]

print(f"A1: {sp.simplify(sol[A1])}")
print(f"B1: {sp.simplify(sol[B1])}")
print(f"A2: {sp.simplify(sol[A2])}")
print(f"B2: {sp.simplify(sol[B2])}")