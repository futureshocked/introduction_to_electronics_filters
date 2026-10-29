import numpy as np
import matplotlib.pyplot as plt

frequencies = np.array([10, 100, 1000, 10000])
gains = np.array([0, -3, -20, -40])

plt.plot(frequencies, gains)
plt.title('Gain vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid(True)
plt.show()
