import matplotlib.pyplot as plt
import numpy as np

# Material constants
D = 1.1 # cm
PHI_0 = 13.1e13 # cm⁻² s⁻1
PI = 3.141592653589
R = 50 # cm

XS_A = 0.107 #cm⁻¹
XS_F = 0.0727
NU = 2.4

# Base phi
def get_phi0(r):
    return (PHI_0 * R * np.sin(PI*r/R))/r

# Current formula
def get_Jr(r):
    return -(D * PHI_0 / (r*r)) * (PI*r*np.cos(PI * r / R) - R*np.sin(PI*r/R))

# Crossing surface at r
def get_crossings(r):
    return 4*PI*r*r * get_Jr(r)

# 8e: Evaluate at specific values of r
Jr_i = get_Jr(R/2 - 0.5)
Jr_o = get_Jr(R/2 + 0.5)
print(get_crossings(R/2 - 0.5))
print(get_crossings(R/2 + 0.5))


# Array
r = np.linspace(0.01, R, 1000)

Jr = get_Jr(r)
Cr = Jr*4*PI*r*r


integ_flux = get_phi0(r)*r*r*4*PI
absorb = integ_flux*XS_A
create = integ_flux*XS_F*NU

# Plots
plt.plot(r, Jr, label="Jr")
plt.plot(r, Cr, label="Cr")
plt.plot(r, get_phi0(r), label="phi")
plt.plot(r, absorb, label="Neutrons absorbed in unit layer")
plt.plot(r, create, label="Neutrons generated in unit layer")

plt.xlabel("r (cm)")
plt.ylabel("Current Jr (cm⁻²s⁻¹) and crossings Cr (s⁻¹)")

plt.legend()
plt.show()

