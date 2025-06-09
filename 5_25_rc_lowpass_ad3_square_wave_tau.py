import numpy as np
import matplotlib.pyplot as plt

# --- RC values ---
R = 2e3           # Ohms
C = 100e-9        # Farads
tau = R * C       # Time constant
print(f"Time constant τ = {tau * 1e6:.1f} µs")

# --- Input waveform parameters ---
Vin = 2           # Volts
f = 500           # Hz
T = 1 / f         # Period
half_T = T / 2

# --- Time vector ---
t = np.linspace(0, 3*T, 3000)

# --- Output voltage calculation ---
Vc = np.zeros_like(t)
Vc_val = 0
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    if (t[i] % T) < half_T:
        Vsource = Vin
    else:
        Vsource = 0
    dVc = (Vsource - Vc_val) * dt / tau
    Vc_val += dVc
    Vc[i] = Vc_val

# --- Plotting ---
plt.figure(figsize=(10, 5))
square_input = Vin * ((t % T) < half_T).astype(float)
plt.plot(t * 1e3, square_input, label='Input (Square Wave)', linestyle='--', color='gray')
plt.plot(t * 1e3, Vc, label='Output (Capacitor Voltage)', color='blue')
plt.title("RC Low-Pass Filter Response to Square Wave")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
