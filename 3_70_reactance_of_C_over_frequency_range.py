import numpy as np
import matplotlib.pyplot as plt

# Define component values
R = 100           # Resistance in Ohms
C = 1e-6          # Capacitance in Farads

# Frequency range: 10 Hz to 1 MHz (logarithmic spacing)
frequencies = np.logspace(1, 6, 500)  # 10^1 to 10^6 Hz

# Calculate reactances
X_R = np.full_like(frequencies, R)                   # Constant for resistor
X_C = 1 / (2 * np.pi * frequencies * C)              # Capacitive reactance

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, X_R, label='Resistor (100 Ω)', linestyle='--')
plt.semilogx(frequencies, X_C, label='Capacitor (1 µF)', linewidth=2)

# Decorations
plt.title('Reactance vs Frequency for Resistor and Capacitor')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Reactance (Ω)')
plt.grid(True, which='both', linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()
