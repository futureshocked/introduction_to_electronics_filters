import numpy as np
import matplotlib.pyplot as plt

# Define component values for RC and RL circuits
R = 1e3      # Resistance in ohms
C = 1e-6     # Capacitance in farads
L = 1e-3     # Inductance in henrys

# Calculate cutoff frequencies
fc_RC = 1 / (2 * np.pi * R * C)
fc_RL = R / (2 * np.pi * L)

# Define frequency range for the plots (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, num=500)
omega = 2 * np.pi * frequencies

# RC filter transfer function magnitude and plot in dB
H_RC = 1 / np.sqrt(1 + (omega * R * C)**2)
H_RC_db = 20 * np.log10(H_RC)

# RL filter transfer function magnitude and plot in dB
H_RL = R / np.sqrt(R**2 + (omega * L)**2)
H_RL_db = 20 * np.log10(H_RL)

# Create subplots for comparison
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# RC filter plot
ax1.semilogx(frequencies, H_RC_db, label="RC Filter")
ax1.axvline(x=fc_RC, color="red", linestyle="--", label=f"RC Cutoff: {fc_RC:.1f} Hz")
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")
ax1.set_title("RC Filter Frequency Response")
ax1.grid(True, which="both", linestyle="--")
ax1.legend()

# RL filter plot
ax2.semilogx(frequencies, H_RL_db, label="RL Filter")
ax2.axvline(x=fc_RL, color="red", linestyle="--", label=f"RL Cutoff: {fc_RL:.1f} Hz")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude (dB)")
ax2.set_title("RL Filter Frequency Response")
ax2.grid(True, which="both", linestyle="--")
ax2.legend()

plt.tight_layout()
plt.show()
