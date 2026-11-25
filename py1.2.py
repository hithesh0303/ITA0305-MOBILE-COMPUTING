import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0.1, 5, 100) 
f = 900                        
Pt = 30                        

fspl = 20*np.log10(d) + 20*np.log10(f) + 32.44
pr_fspl = Pt - fspl

n = 3.5
d0 = 0.1
PL0 = 20*np.log10(d0) + 20*np.log10(f) + 32.44

pl = PL0 + 10*n*np.log10(d/d0)
pr_log = Pt - pl

plt.plot(d, pr_fspl, label="Free Space Model")
plt.plot(d, pr_log, label="Log-Distance Model (n=3.5)")

plt.xlabel("Distance (km)")
plt.ylabel("Received Power (dBm)")
plt.title("Free Space vs Log-Distance Path Loss at 900 MHz")
plt.legend()
plt.grid(True)
plt.show()

print("Free Space Model:")
print("Received power at 0.1 km:", round(pr_fspl[0], 2), "dBm")
print("Received power at 5 km:", round(pr_fspl[-1], 2), "dBm")

print("\nLog-Distance Model:")
print("Received power at 0.1 km:", round(pr_log[0], 2), "dBm")
print("Received power at 5 km:", round(pr_log[-1], 2), "dBm")
