import numpy as np
import matplotlib.pyplot as plt

# Define resistor value
R = 1e3  # Resistance in ohms

# Define a range of capacitor values (in farads)
capacitor_values = [0.1e-6, 1e-6, 10e-6]

# Define frequency range (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, num=500)
omega = 2 * np.pi * frequencies

plt.figure(figsize=(8, 4))

# Loop over capacitor values and plot phase shift
for C in capacitor_values:
    phase_rad = -np.arctan(omega * R * C)
    phase_deg = np.degrees(phase_rad)
    plt.semilogx(frequencies, phase_deg, label=f"C = {C*1e6:.1f} µF")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase Shift (degrees)")
plt.title("Effect of Capacitor Value on Phase Shift in an RC Low-Pass Filter")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()
