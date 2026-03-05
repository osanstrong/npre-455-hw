import matplotlib.pyplot as plt
import numpy as np
from numpy import sinh, cosh


PI = np.pi

D = 2 # cm
S = 1e10 #n/cm^3/s
L = 5 # cm
X_a = D / (L**2) # 1/cm
X_ap = 3 # 1/cm

a = 50 # cm
at = a + 2*D
b = 0.1 # cm
c = 20 # cm

N_STEPS = 16*10*4
x = np.linspace(0, a, N_STEPS)
def get_cstep(c):
    return int(N_STEPS * c/a + 0.5) #round just to be extra safe

def gen_coeffs():
    A1 =  -S*(2*D*sinh(D/L)**2 - D*cosh(at/L) + D + 2*L*X_ap*b*sinh(D/L)**2*sinh((at - c)/L) - L*X_ap*b*sinh(c/L)*sinh((at - c)/L) + L*X_ap*b*sinh((at - c)/L))/(X_a*(2*D*sinh(D/L)*cosh((D + at)/L) + D*sinh(at/L) + 2*L*X_ap*b*sinh(D/L)**2*sinh(c/L)*sinh((at - c)/L) + 2*L*X_ap*b*sinh(D/L)*sinh(c/L)*sinh((at - c)/L)*cosh(D/L) + L*X_ap*b*sinh(c/L)*sinh((at - c)/L)))
    B1 =  -S*(D*sinh(2*D/L) + D*sinh(at/L) + L*X_ap*b*cosh(at/L)/2 - L*X_ap*b*cosh((at - 2*c)/L)/2 - L*X_ap*b*cosh((2*D - at + c)/L)/2 + L*X_ap*b*cosh((2*D + at - c)/L)/2)/(X_a*(2*D*sinh(D/L)*cosh((D + at)/L) + D*sinh(at/L) + 2*L*X_ap*b*sinh(D/L)**2*sinh(c/L)*sinh((at - c)/L) + 2*L*X_ap*b*sinh(D/L)*sinh(c/L)*sinh((at - c)/L)*cosh(D/L) + L*X_ap*b*sinh(c/L)*sinh((at - c)/L)))
    A2 =  S*(-D*cosh(2*D/L) + D*cosh(at/L) + L*X_ap*b*sinh(2*(D - c)/L)/4 - L*X_ap*b*sinh(2*(D + c)/L)/4 - L*X_ap*b*sinh((at - 2*c)/L)/4 + L*X_ap*b*sinh((at + 2*c)/L)/4 + L*X_ap*b*sinh((2*D - at + c)/L)/2 + L*X_ap*b*sinh((2*D + at + c)/L)/2 + L*X_ap*b*cosh(at/L)/2 + L*X_ap*b*cosh(2*(D - c)/L)/4 - L*X_ap*b*cosh(2*(D + c)/L)/4 - L*X_ap*b*cosh((at - 2*c)/L)/4 - L*X_ap*b*cosh((at + 2*c)/L)/4)/(X_a*(2*D*sinh(D/L)*cosh((D + at)/L) + D*sinh(at/L) + 2*L*X_ap*b*sinh(D/L)**2*sinh(c/L)*sinh((at - c)/L) + 2*L*X_ap*b*sinh(D/L)*sinh(c/L)*sinh((at - c)/L)*cosh(D/L) + L*X_ap*b*sinh(c/L)*sinh((at - c)/L)))
    B2 =  -S*(2*D*sinh(D/L)*cosh(D/L) + D*sinh(at/L) - 2*L*X_ap*b*sinh(D/L)**2*sinh(c/L)**2 + 2*L*X_ap*b*sinh(D/L)*sinh(at/L)*cosh((D + c)/L) - 2*L*X_ap*b*sinh(D/L)*sinh(c/L)**2*cosh(D/L) - L*X_ap*b*sinh(at/L)*sinh(c/L)**2 + L*X_ap*b*sinh(at/L)*sinh(c/L)*cosh(c/L) + L*X_ap*b*sinh(at/L)*sinh(c/L) - L*X_ap*b*sinh(c/L)**2)/(X_a*(2*D*sinh(D/L)*cosh((D + at)/L) + D*sinh(at/L) + 2*L*X_ap*b*sinh(D/L)**2*sinh(c/L)*sinh((at - c)/L) + 2*L*X_ap*b*sinh(D/L)*sinh(c/L)*sinh((at - c)/L)*cosh(D/L) + L*X_ap*b*sinh(c/L)*sinh((at - c)/L)))
    return A1, B1, A2, B2

A1, B1, A2, B2 = gen_coeffs()

def get_flux(c):
    A1, B1, A2, B2 = gen_coeffs()
    c_idx = get_cstep(c)
    left = x[:c_idx]
    right = x[c_idx:]

    flux = np.zeros(N_STEPS)
    flux[:c_idx] = A1*sinh(left/L) + B1*cosh(left/L) + S/X_a
    flux[c_idx:] = A2*sinh(right/L)+ B2*cosh(right/L)+ S/X_a
    return flux

# # Original parameters
# plt.title("Problem 3 c")
# plt.plot(x, get_flux(20), label="Flux (original parameters)")
# plt.xlabel("x (cm)")
# plt.ylabel("Flux (1/cm^2/s)")

# plt.legend()
# plt.show()


# Varying X_ap
# plt.title("Problem 3 d")
# for newX in [0, 1.5, 3.0, 6.0, 12.0]:
#     X_ap = newX
#     plt.plot(x, get_flux(20), label=f"Flux (XC_ap = {newX})")
# plt.xlabel("x (cm)")
# plt.ylabel("Flux (1/cm^2/s)")

# plt.legend()
# plt.show()

# Varying location
plt.title("Problem 3 e")
X_ap = 0
plt.plot(x, get_flux(20), label=f"Flux (XC_ap = 0)")
X_ap = 3.0
for newC in [a/16, a/8, a/4, a/2]:
    c = newC
    plt.plot(x, get_flux(c), label=f"Flux (c = {c}cm)")
plt.xlabel("x (cm)")
plt.ylabel("Flux (1/cm^2/s)")

plt.legend()
plt.show()