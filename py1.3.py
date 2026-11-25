import numpy as np

f = 900
Pt = 30
n = 3.5
d0 = 0.1
Pr_min = -90

PL0 = 20*np.log10(d0) + 20*np.log10(f) + 32.44

d_max = d0 * 10**((Pt - Pr_min - PL0) / (10*n))

print("Maximum communication distance:", round(d_max, 2), "km")
print("Receiver sensitivity:", Pr_min, "dBm")
