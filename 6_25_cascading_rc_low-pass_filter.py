import numpy as np
import matplotlib.pyplot as plt

# RC values
R = 1e3         # 1 kΩ
C = 0.159e-6    # 0.159 µF, gives fc ≈ 1kHz
f = np.logspace(1, 6, 500)  # Frequency from 10Hz to 1MHz

fc = 1/(2*np.pi*R*C)
H_single = 1 / (1 + 1j*(f/fc))
H_cascade = H_single ** 2

plt.figure(figsize=(8,5))
plt.semilogx(f, 20*np.log10(abs(H_single)), label='Single-stage')
plt.semilogx(f, 20*np.log10(abs(H_cascade)), label='Two-stage Cascade')
plt.title('Cascaded RC Low-pass Filter Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', linestyle='--')
plt.axvline(fc, color='grey', linestyle=':', label=f'$f_c$={fc:.0f} Hz')
plt.legend()
plt.show()
