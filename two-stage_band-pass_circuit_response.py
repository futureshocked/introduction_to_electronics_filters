import numpy as np
import matplotlib.pyplot as plt

# Define RC values
R_HP = 1.3e3        # 1.3 kΩ
C_HP = 0.47e-6      # 0.47 µF
R_LP = 3.9e3        # 3.9 kΩ
C_LP = 10e-9        # 10 nF

# Calculate cutoff frequencies for reference
fc_HP = 1/(2*np.pi*R_HP*C_HP)
fc_LP = 1/(2*np.pi*R_LP*C_LP)

print(f"High-pass cutoff frequency: {fc_HP:.1f} Hz")
print(f"Low-pass cutoff frequency: {fc_LP:.1f} Hz")

# Frequency range for plotting
f = np.logspace(1, 5, 500)  # from 10 Hz to 100 kHz

# Calculate frequency response
H_HP = (1j*(f/fc_HP)) / (1 + 1j*(f/fc_HP))
H_LP = 1 / (1 + 1j*(f/fc_LP))

# Combined band-pass filter response
H_BP = H_HP * H_LP

# Plotting
plt.figure(figsize=(8, 5))
plt.semilogx(f, 20*np.log10(np.abs(H_BP)), label='Band-pass response')
plt.axvline(fc_HP, color='grey', linestyle='--', label=f'$f_{{HP}}$ ≈ {fc_HP:.0f} Hz')
plt.axvline(fc_LP, color='grey', linestyle=':', label=f'$f_{{LP}}$ ≈ {fc_LP:.0f} Hz')

plt.title('Band-pass Filter for Voice Frequencies (300–3400 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
