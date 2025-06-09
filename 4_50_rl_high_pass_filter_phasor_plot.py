import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R_rl = 470  # 470 Ohms
L_rl = 10e-3  # 10 mH

# Selected frequencies (Hz)
frequencies_rl = np.array([10, 50, 7500, 10000, 50000])
omega_rl = 2 * np.pi * frequencies_rl

# Transfer function H(jω)
H_rl = (1j * omega_rl * L_rl) / (R_rl + 1j * omega_rl * L_rl)

# Magnitude and phase
magnitude_rl = np.abs(H_rl)
phase_rl = np.angle(H_rl, deg=True)

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
for i in range(len(frequencies_rl)):
    ax.arrow(0, 0,
             magnitude_rl[i] * np.cos(np.deg2rad(phase_rl[i])),
             magnitude_rl[i] * np.sin(np.deg2rad(phase_rl[i])),
             head_width=0.02, head_length=0.04,
             fc='red', ec='red')
    ax.text(magnitude_rl[i] * np.cos(np.deg2rad(phase_rl[i])) * 1.1,
            magnitude_rl[i] * np.sin(np.deg2rad(phase_rl[i])) * 1.1,
            f"{frequencies_rl[i]} Hz", fontsize=8)

ax.plot([], [], 'r-', label='Phasor (origin to tip)')
ax.set_title("Phasor Plot – RL High-Pass Filter (Corrected)")
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.grid(True)
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.legend()
plt.tight_layout()
plt.show()
