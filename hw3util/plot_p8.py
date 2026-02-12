import matplotlib.pyplot as plt
import numpy as np

# Material constants
D = 1.1 # cm
PHI_0 = 13.1e13 # cm⁻² s⁻1
PI = 3.141592653589
R = 50 # cm

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
r = np.linspace(1, R, 1000)

Jr = get_Jr(r)

# Plots
plt.plot(r, Jr, label="Jr")

plt.xlabel("r (cm)")
plt.ylabel("Current Jr (cm⁻²s⁻¹)")

plt.legend()
plt.show()

