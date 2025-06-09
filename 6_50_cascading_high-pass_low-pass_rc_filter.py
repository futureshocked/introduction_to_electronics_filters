import numpy as np
import matplotlib.pyplot as plt

# RC values
R_HP = 1300
C_HP = 0.47e-6

R_LP = 3900
C_LP = 10e-9

f = np.logspace(1, 6, 500)  # Frequency from 10 Hz to 1 MHz

# Calculate cutoff frequencies
fc_HP = 1/(2*np.pi*R_HP*C_HP)
fc_LP = 1/(2*np.pi*R_LP*C_LP)

# Individual filter responses
H_HP = (1j*(f/fc_HP)) / (1 + 1j*(f/fc_HP))
H_LP = 1 / (1 + 1j*(f/fc_LP))

# Cascaded band-pass response
H_BP = H_HP * H_LP

# Plot response
plt.figure(figsize=(8,5))
plt.semilogx(f, 20*np.log10(abs(H_BP)), label='Band-pass (HP+LP)')
plt.axvline(fc_HP, color='grey', linestyle='--', label=f'$f_{{HP}}$ = {fc_HP:.0f} Hz')
plt.axvline(fc_LP, color='grey', linestyle=':', label=f'$f_{{LP}}$ = {fc_LP:.0f} Hz')
plt.title('Band-pass Filter Response (High-pass + Low-pass)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.show()
