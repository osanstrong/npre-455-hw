import numpy as np
import matplotlib.pyplot as plt
from numpy import sinh, cosh, exp

S = 1e10 #/s
D = 0.9 #cm
SIG_A = 0.5 # /cm
R = 100 #cm
RT = R+2*D #cm, extrapolated
L = np.sqrt(D/SIG_A) #cm

PI = 3.141692653589

def get_flux(r):
    return (S/(4*PI*D*np.sinh(RT/L)))*(np.sinh((RT-r)/L) / r)

def get_flux_Rob(r):
    A = -S*(-2*D*L*cosh(R/L) + 2*D*R*sinh(R/L) + L*R*cosh(R/L))/(4*PI*D*(-2*D*L*sinh(R/L) + 2*D*R*cosh(R/L) + L*R*sinh(R/L)))
    B = S/(4*PI*D)
    
    return (A*sinh(R/L) + B*cosh(R/L))/r


r_d = np.linspace(1,R,1000)
F_d = get_flux(r_d)


# plt.plot(r_d, F_d*4*PI*r_d*r_d, label="Flux of part d")
# plt.xlabel("r (cm)")
# plt.ylabel("Flux (1/cm²/s)")
# plt.legend()
# plt.show()


R = 1.5
S = 100
SIG_A = 0.026
D = 0.79
RT = R+2*D
L = np.sqrt(D/SIG_A)

def get_flux(r):
    return (S/(4*PI*D*np.sinh(RT/L)))*(np.sinh((RT-r)/L) / r)

def get_flux_Rob2(r):
    A = -S*(-2*D*L*cosh(R/L) + 2*D*R*sinh(R/L) + L*R*cosh(R/L))/(4*PI*D*(-2*D*L*sinh(R/L) + 2*D*R*cosh(R/L) + L*R*sinh(R/L)))
    B = S/(4*PI*D)
    phi = (A*sinh(R/L) + B*cosh(R/L))/r
    print(phi)
    return phi

r_f = np.linspace(0.01*R, R, 1001)
F_f = get_flux(r_f)
FR_f = get_flux_Rob2(r_f)



# plt.plot(r_f, F_f, label="Extrapolated flux")
# plt.plot(r_f, FR_f, label="Robin condition")
# plt.xlabel("r (cm)")
# plt.ylabel("Flux (1/cm²/s)")
# plt.legend()
# plt.show()


D1 = 0.1
D2 = 0.8
L1 = 1.0
L2 = 7.0
a = 20
at = a + 2*D1
b = 30
bt = b + 2*D2
S = 1e10


def get_flux1(x):
    B1 = -at
    A1 = 2*L1*L2*S*(1 - exp(2*bt/L2))*exp(at/L1)/(-D1*L2*exp(2*at/L1) + D1*L2*exp(2*bt/L2) + D1*L2*exp(2*bt/L2 + 2*at/L1) - D1*L2 + D2*L1*exp(2*at/L1) - D2*L1*exp(2*bt/L2) + D2*L1*exp(2*bt/L2 + 2*at/L1) - D2*L1)
    f1 = A1*sinh((B1-x)/L1)
    return f1

def get_flux2(x):
    B2 = bt
    A2 = -2*L1*L2*S*(exp(2*at/L1) - 1)*exp(bt/L2)/(D1*L2*exp(2*at/L1) - D1*L2*exp(2*bt/L2) - D1*L2*exp(2*bt/L2 + 2*at/L1) + D1*L2 - D2*L1*exp(2*at/L1) + D2*L1*exp(2*bt/L2) - D2*L1*exp(2*bt/L2 + 2*at/L1) + D2*L1)
    f2 = A2*sinh((B2-x)/L2)
    return f2

x1 = np.linspace(-a, 0, 1000)
x2 = np.linspace(0, b, 2000)

f1 = get_flux1(x1)
f2 = get_flux2(x2)

plt.plot(x1, f1, label="Region A")
plt.plot(x2, f2, label="Region B")
plt.xlabel("x (cm)")
plt.ylabel("Flux (1/cm²/s)")
plt.legend()
plt.show()