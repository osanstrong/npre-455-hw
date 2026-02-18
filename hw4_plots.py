import numpy as np
import matplotlib.pyplot as plt

S = 1e10 #/s
D = 0.9 #cm
SIG_A = 0.5 # /cm
R = 100 #cm
RT = R+2*D #cm, extrapolated
L = np.sqrt(D/SIG_A) #cm

PI = 3.141692653589

def get_flux(r):
    return (S/(4*PI*D*np.sinh(RT/L)))*(np.sinh((RT-r)/L) / r)


r_d = np.linspace(1,R,1000)
F_d = get_flux(r_d)

plt.plot(r_d, F_d*4*PI*r_d*r_d, label="Flux of part d")
plt.xlabel("r (cm)")
plt.ylabel("Flux (1/cm²/s)")
plt.legend()
plt.show()