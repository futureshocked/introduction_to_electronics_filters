import numpy as np
import matplotlib.pyplot as plt

# Define resistor and capacitor values
R = 1e3      # Resistance in ohms
C = 1e-6     # Capacitance in farads

# Calculate the cutoff frequency
fc = 1 / (2 * np.pi * R * C)

# Define specific frequency points
f_low = 10         # Low frequency in Hz
f_high = 100e3     # High frequency in Hz

# Calculate angular frequencies for these points
omega_low = 2 * np.pi * f_low
omega_fc = 2 * np.pi * fc
omega_high = 2 * np.pi * f_high

# Calculate transfer function magnitudes at these frequencies
H_low = 1 / np.sqrt(1 + (omega_low * R * C)**2)
H_fc = 1 / np.sqrt(1 + (omega_fc * R * C)**2)
H_high = 1 / np.sqrt(1 + (omega_high * R * C)**2)

# Print the calculated magnitudes
print(f"Low Frequency ({f_low} Hz): |H(jω)| ≈ {H_low:.3f}")
print(f"Cutoff Frequency ({fc:.2f} Hz): |H(jω)| ≈ {H_fc:.3f}")
print(f"High Frequency ({f_high} Hz): |H(jω)| ≈ {H_high:.3f}")

# Define frequency range for plotting (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, num=500)
omega = 2 * np.pi * frequencies

# Calculate the magnitude of the transfer function over the frequency range
H_mag = 1 / np.sqrt(1 + (omega * R * C)**2)
H_db = 20 * np.log10(H_mag)

# Create the plot
plt.figure(figsize=(8, 4))
plt.semilogx(frequencies, H_db, label="RC Low-Pass Filter Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Frequency Response of RC Low-Pass Filter")

# Mark the calculated frequency points
plt.plot(f_low, 20 * np.log10(H_low), 'ro', label=f"Low ({f_low} Hz)")
plt.plot(fc, 20 * np.log10(H_fc), 'go', label=f"Cutoff ({fc:.1f} Hz)")
plt.plot(f_high, 20 * np.log10(H_high), 'bo', label=f"High ({f_high} Hz)")

plt.legend()
plt.grid(True, which="both", linestyle="--")
plt.show()
