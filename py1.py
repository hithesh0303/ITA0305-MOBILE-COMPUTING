import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0.1, 5, 100)  
f = 1800


fspl = 20*np.log10(d) + 20*np.log10(f) + 32.44

pr = 30 - fspl                

plt.plot(d, pr)
plt.xlabel("Distance (km)")
plt.ylabel("Received Power (dBm)")
plt.title("Free-Space Path Loss at 1800 MHz")
plt.grid(True)
plt.show()

print("Received power at 0.1 km :", round(pr[0], 2), "dBm")
print("Received power at 5 km   :", round(pr[-1], 2), "dBm")
