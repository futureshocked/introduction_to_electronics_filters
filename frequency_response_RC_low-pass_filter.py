import numpy as np
import matplotlib.pyplot as plt

# Define resistor and capacitor values
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads

# Calculate the cutoff frequency
fc = 1 / (2 * np.pi * R * C)

# Define frequency range for the plot (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, num=500)
omega = 2 * np.pi * frequencies

# Calculate the magnitude of the transfer function for the low-pass filter
H_mag = 1 / np.sqrt(1 + (omega * R * C)**2)
H_db = 20 * np.log10(H_mag)

# Create the plot
plt.figure(figsize=(8, 4))
plt.semilogx(frequencies, H_db)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Frequency Response of RC Low-Pass Filter")
plt.grid(True, which="both", linestyle="--")

# Mark the cutoff frequency with a red dashed line
plt.axvline(x=fc, color="red", linestyle="--", label=f"Cutoff Frequency: {fc:.1f} Hz")
plt.legend()

plt.show()
