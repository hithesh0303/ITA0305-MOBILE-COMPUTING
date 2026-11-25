import matplotlib.pyplot as plt

def erlang_b(A, C):                       # A = traffic in Erlangs, C = channels
    B = 1.0
    for k in range(1, C + 1):
        B = A * B / (k + A * B)
    return B

channels = range(1, 26)
for A in (5, 10, 15):
    plt.plot(channels, [erlang_b(A, c) for c in channels], label=f"A = {A} Erlang")
plt.xlabel("Channels"); plt.ylabel("Blocking probability")
plt.legend(); plt.grid(True); plt.show()
print("Blocking for A=10, C=15:", round(erlang_b(10, 15), 4))
