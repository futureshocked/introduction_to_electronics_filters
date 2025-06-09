import numpy as np
import matplotlib.pyplot as plt

# Define resistor and capacitor values
R = 1e3      # Resistance in ohms
C = 1e-6     # Capacitance in farads

# Define frequency range (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, num=500)
omega = 2 * np.pi * frequencies

# Calculate phase shift in radians for an RC low-pass filter: φ = -arctan(ωRC)
phase_rad = -np.arctan(omega * R * C)

# Convert phase shift to degrees
phase_deg = np.degrees(phase_rad)

# Create the plot
plt.figure(figsize=(8, 4))
plt.semilogx(frequencies, phase_deg)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase Shift (degrees)")
plt.title("Phase Shift of an RC Low-Pass Filter")
plt.grid(True, which="both", linestyle="--")
plt.show()
