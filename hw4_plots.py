import numpy as np
import matplotlib.pyplot as plt
from numpy import sinh, cosh

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

def get_flux2(r):
    return (S/(4*PI*D*np.sinh(RT/L)))*(np.sinh((RT-r)/L) / r)

def get_flux_Rob2(r):
    A = -S*(-2*D*L*cosh(R/L) + 2*D*R*sinh(R/L) + L*R*cosh(R/L))/(4*PI*D*(-2*D*L*sinh(R/L) + 2*D*R*cosh(R/L) + L*R*sinh(R/L)))
    B = S/(4*PI*D)
    phi = (A*sinh(R/L) + B*cosh(R/L))/r
    print(phi)
    return phi

r_f = np.linspace(0.01*R, R, 1001)
F_f = get_flux2(r_f)
FR_f = get_flux_Rob2(r_f)



plt.plot(r_f, F_f, label="Extrapolated flux")
plt.plot(r_f, FR_f, label="Robin condition")
plt.xlabel("r (cm)")
plt.ylabel("Flux (1/cm²/s)")
plt.legend()
plt.show()

