import numpy as np
import matplotlib.pyplot as plt

N = np.array([3, 4, 7, 9, 12])
gamma, total = 4, 336
Q = np.sqrt(3 * N)                        # co-channel reuse ratio D/R
ch = total / N                            # channels per cell
si_db = 10 * np.log10(Q**gamma / 6)       # first-tier S/I in dB (6 interferers)

print("N    Q    ch/cell  S/I(dB)")
for n, q, c, s in zip(N, Q, ch, si_db):
    print(f"{n:<4d} {q:5.2f} {c:7.1f} {s:7.2f}")

plt.plot(N, si_db, "o-")
plt.axhline(18, linestyle="--", color="r", label="18 dB (AMPS requirement)")
plt.xlabel("Cluster size N"); plt.ylabel("S/I (dB)")
plt.legend(); plt.grid(True); plt.show()
