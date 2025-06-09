import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- Parameters ---
R = 470  # Ohms
fc = 3400  # Hz
omega_c = 2 * np.pi * fc
L = R / omega_c  # Henries

print(f"Calculated L = {L*1000:.2f} mH")

# Frequency range for Bode plot
f = np.logspace(2, 5, 500)  # from 100 Hz to 100 kHz
omega = 2 * np.pi * f

# Transfer function
H = 1j * omega * L / (R + 1j * omega * L)

# Magnitude and phase
magnitude = np.abs(H)
magnitude_db = 20 * np.log10(magnitude)
phase = np.angle(H, deg=True)

# --- Bode Magnitude Plot ---
fig, ax = plt.subplots()
ax.semilogx(f, magnitude_db)
ax.set_title("Bode Magnitude Plot – RL High-Pass Filter")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.grid(which='both', linestyle='--', linewidth=0.5)
ax.axvline(fc, color='red', linestyle='--', label=f"Cutoff {fc} Hz")
ax.legend()
plt.tight_layout()
plt.show()

# --- Bode Phase Plot ---
fig, ax = plt.subplots()
ax.semilogx(f, phase)
ax.set_title("Bode Phase Plot – RL High-Pass Filter")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Phase (degrees)")
ax.grid(which='both', linestyle='--', linewidth=0.5)
ax.axvline(fc, color='red', linestyle='--', label=f"Cutoff {fc} Hz")
ax.legend()
plt.tight_layout()
plt.show()

# --- Phasor Plot at Selected Frequencies ---
sample_freqs = np.array([100, 1000, 3400, 10000, 50000])
sample_omega = 2 * np.pi * sample_freqs
sample_H = 1j * sample_omega * L / (R + 1j * sample_omega * L)
sample_mags = np.abs(sample_H)
sample_phases = np.angle(sample_H, deg=True)

fig, ax = plt.subplots(figsize=(6, 6))
for i in range(len(sample_freqs)):
    ax.arrow(0, 0,
             sample_mags[i] * np.cos(np.deg2rad(sample_phases[i])),
             sample_mags[i] * np.sin(np.deg2rad(sample_phases[i])),
             head_width=0.02, head_length=0.04,
             fc='red', ec='red')
    ax.text(sample_mags[i] * np.cos(np.deg2rad(sample_phases[i])) * 1.1,
            sample_mags[i] * np.sin(np.deg2rad(sample_phases[i])) * 1.1,
            f"{sample_freqs[i]} Hz", fontsize=8)

ax.plot([], [], 'r-', label='Phasor (origin to tip)')
ax.set_title("Phasor Plot – RL High-Pass Filter")
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.grid(True)
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.legend()
plt.tight_layout()
plt.show()

# --- Print table of magnitude and phase for selected frequencies ---
df = pd.DataFrame({
    "Frequency (Hz)": sample_freqs,
    "Magnitude": np.round(sample_mags, 4),
    "Phase (°)": np.round(sample_phases, 2)
})
print(df)
