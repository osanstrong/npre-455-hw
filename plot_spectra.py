import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# spec1 = pd.read_csv("hw2flux/flux_spectrum1.csv")
# print(spec1.columns)
# print(spec1['flux'])
# spec1["bw"] = spec1["Emax"]-spec1["Emin"]
# spec1["ul"] = np.log(spec1["Emax"]/spec1["Emin"])
# print(spec1)


# fig, ax = plt.subplots()
# ax.set_xlabel("Energy (eV)")
# # ax.set_ylabel("Flux normalized by bin width (1/cm²/s/eV)")
# ax.set_ylabel("Flux normalized per unit lethargy (1/cm²/s)")

# # ax.plot(spec1["Emax"], spec1["flux"]/spec1["bw"])
# ax.plot(spec1["Emax"], spec1["flux"]/spec1["ul"])
# ax.loglog()

# fig.legend()
# plt.show()

spec3 = pd.read_csv("hw2flux/flux_spectrum3.csv")
print(spec3.columns)
print(spec3['flux'])
spec3["ul"] = np.log(spec3["Emax"]/spec3["Emin"])
print(spec3)


fig, ax = plt.subplots()
ax.set_xlabel("Energy (eV)")
ax.set_ylabel("Flux normalized per unit lethargy (1/cm²/s)")

ax.plot(spec3["Emax"], spec3["flux"]/spec3["ul"])
ax.loglog()

fig.legend()
plt.show()