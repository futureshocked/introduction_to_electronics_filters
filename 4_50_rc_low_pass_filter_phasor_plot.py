import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R_rc = 1e3  # 1 kOhm
C_rc = 1e-6  # 1 uF
RC_time = R_rc * C_rc

# Selected frequencies (Hz)
frequencies_rc = np.array([10, 50, 159, 1000, 5000])
omega_rc = 2 * np.pi * frequencies_rc

# Transfer function H(jω)
H_rc = 1 / (1 + 1j * omega_rc * RC_time)

# Magnitude and phase
magnitude_rc = np.abs(H_rc)
phase_rc = np.angle(H_rc, deg=True)

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
for i in range(len(frequencies_rc)):
    ax.arrow(0, 0,
             magnitude_rc[i] * np.cos(np.deg2rad(phase_rc[i])),
             magnitude_rc[i] * np.sin(np.deg2rad(phase_rc[i])),
             head_width=0.02, head_length=0.04,
             fc='blue', ec='blue')
    ax.text(magnitude_rc[i] * np.cos(np.deg2rad(phase_rc[i])) * 1.1,
            magnitude_rc[i] * np.sin(np.deg2rad(phase_rc[i])) * 1.1,
            f"{frequencies_rc[i]} Hz", fontsize=8)

ax.plot([], [], 'b-', label='Phasor (origin to tip)')
ax.set_title("Phasor Plot – RC Low-Pass Filter (Corrected)")
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.grid(True)
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 0.2)
ax.legend()
plt.tight_layout()
plt.show()
