import numpy as np
import matplotlib.pyplot as plt

# Define resistor and inductor values
R = 1e3  # Resistance in ohms
L = 1e-3  # Inductance in henrys

# Calculate the cutoff frequency
fc = R / (2 * np.pi * L)

# Define frequency range for the plot (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, num=500)
omega = 2 * np.pi * frequencies

# Calculate the magnitude of the transfer function for the low-pass filter
H_mag = R / np.sqrt(R**2 + (omega * L)**2)
H_db = 20 * np.log10(H_mag)

# Create the plot
plt.figure(figsize=(8, 4))
plt.semilogx(frequencies, H_db)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Frequency Response of RL Low-Pass Filter")
plt.grid(True, which="both", linestyle="--")

# Mark the cutoff frequency with a red dashed line
plt.axvline(x=fc, color="red", linestyle="--", label=f"Cutoff Frequency: {fc:.1f} Hz")
plt.legend()

plt.show()
