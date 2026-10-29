import numpy as np
import matplotlib.pyplot as plt

frequencies = np.array([10, 100, 1000, 10000])
gains = np.array([0, -3, -20, -40])

plt.semilogx(frequencies, gains)
plt.grid(True, which='both')
fc = 1000  # Example cutoff frequency
plt.axvline(fc, color='red', linestyle='--', label=f'Cutoff at {fc} Hz')
plt.show()
