import numpy as np
import matplotlib.pyplot as plt

# Define RC values for a high-pass and a low-pass filter
R_HP = 1e3          # 1 kΩ
C_HP = 0.159e-6     # 0.159 µF, fc_HP ≈ 1 kHz

R_LP = 1e3          # 1 kΩ
C_LP = 15.9e-9      # 15.9 nF, fc_LP ≈ 10 kHz

# Generate frequency points from 10 Hz to 1 MHz
f = np.logspace(1, 6, 500)

# Calculate cutoff frequencies
fc_HP = 1 / (2 * np.pi * R_HP * C_HP)
fc_LP = 1 / (2 * np.pi * R_LP * C_LP)

# Calculate individual filter responses
H_HP = (1j * (f / fc_HP)) / (1 + 1j * (f / fc_HP))
H_LP = 1 / (1 + 1j * (f / fc_LP))

# Calculate combined band-pass response
H_BP = H_HP * H_LP

# Plot the magnitude response
plt.figure(figsize=(8,5))
plt.semilogx(f, 20 * np.log10(abs(H_BP)), label='Band-pass (HP + LP)')

# Add cutoff frequency lines
plt.axvline(fc_HP, color='grey', linestyle='--', label=f'$f_{{HP}}$ = {fc_HP:.0f} Hz')
plt.axvline(fc_LP, color='grey', linestyle=':', label=f'$f_{{LP}}$ = {fc_LP:.0f} Hz')

# Add labels, title, grid, and legend
plt.title('Band-pass Filter Response (High-pass + Low-pass)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', linestyle='--')
plt.legend()

# Show the plot
plt.show()
