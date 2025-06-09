import numpy as np
import matplotlib.pyplot as plt

# Define parameters
R = 1000           # Resistance in ohms
C = 1e-6           # Capacitance in farads
tau = R * C
f_c = 1 / (2 * np.pi * tau)

# Frequency range
frequencies = np.logspace(1, 5, 500)  # 10 Hz to 100 kHz
omega = 2 * np.pi * frequencies

# Calculate transfer functions
H_lowpass = 1 / np.sqrt(1 + (omega * tau)**2)
H_highpass = (omega * tau) / np.sqrt(1 + (omega * tau)**2)

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, 20 * np.log10(H_lowpass), label='Low-Pass Filter')
plt.semilogx(frequencies, 20 * np.log10(H_highpass), label='High-Pass Filter')
plt.axvline(f_c, color='gray', linestyle='--', label=f'Cutoff Frequency {f_c:.1f} Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.title('Frequency Response of RC Audio Filters')
plt.grid(True, which='both', linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()
