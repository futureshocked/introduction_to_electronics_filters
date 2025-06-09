import numpy as np
import matplotlib.pyplot as plt

# RC values
R_HP = 10e3          # 10 kΩ
C_HP = 0.159e-9     # 0.159 nF, fc_HP ≈ 1 kHz

R_LP = 1e3          # 1 kΩ
C_LP = 15.9e-9      # 15.9 nF, fc_LP ≈ 10 kHz

f = np.logspace(2, 5, 500)  # Frequency from 10 Hz to 1 MHz

# Calculate cutoff frequencies
fc_HP = 1/(2*np.pi*R_HP*C_HP)
fc_LP = 1/(2*np.pi*R_LP*C_LP)

# Individual filter responses
H_HP = (1j*(f/fc_HP)) / (1 + 1j*(f/fc_HP))
H_LP = 1 / (1 + 1j*(f/fc_LP))

# Cascaded band-pass response
H_BP = H_HP * H_LP

print(fc_HP)
print(fc_LP)

# Plot response
plt.figure(figsize=(8,5))
#plt.semilogx(f, 20*np.log10(abs(H_BP)), label='Band-pass (HP+LP)')
plt.semilogx(f, 20*np.log10(abs(H_LP)), label='Low-pass only')
#plt.semilogx(f, 20 * np.log10(abs(H_BP)), color='red', linestyle='-', linewidth=2, label='Band-pass (HP + LP)')
plt.axvline(fc_HP, color='red', linestyle='--', label=f'$f_{{HP}}$ = {fc_HP:.0f} Hz')
plt.axvline(fc_LP, color='orange', linestyle=':', label=f'$f_{{LP}}$ = {fc_LP:.0f} Hz')
#plt.title('Band-pass Filter Response (High-pass + Low-pass)')
plt.title('Low-pass Filter Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', linestyle='--')
plt.text(fc_HP, -30, 'HP example 1', ha='right')
plt.text(fc_LP, -40, 'LP example 2', ha='left')
plt.legend()
plt.show()
