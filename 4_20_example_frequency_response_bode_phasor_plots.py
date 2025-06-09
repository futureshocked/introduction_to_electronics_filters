import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Filter Parameters ---
R = 1000         # Resistance in Ohms
L = 10e-3        # Inductance in Henrys
tau = L / R      # Time constant

# --- Frequency Range ---
frequencies = np.linspace(10, 10000, 1000)  # Linear space: 10 Hz to 10 kHz
omega = 2 * np.pi * frequencies             # Angular frequency (rad/s)

# --- Transfer Function H(jω) for RL low-pass filter ---
# H(jω) = R / (R + jωL)
H_jw = R / (R + 1j * omega * L)

# --- Magnitude and Phase ---
magnitude = np.abs(H_jw)
phase = np.angle(H_jw, deg=True)

# --- Frequency Response Plot (Linear) ---
plt.figure(figsize=(10, 4))

# Magnitude plot
plt.subplot(1, 2, 1)
plt.plot(frequencies, magnitude)
plt.title("Frequency Response (Magnitude)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (V/V)")
plt.grid(True)

# Phase plot
plt.subplot(1, 2, 2)
plt.plot(frequencies, phase)
plt.title("Frequency Response (Phase)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Bode Plot (Log frequency, dB magnitude) ---
w, mag_db, phase_deg = signal.bode(signal.TransferFunction([R], [L, R]), omega)

plt.figure(figsize=(10, 4))

# Bode Magnitude
plt.subplot(1, 2, 1)
plt.semilogx(w / (2 * np.pi), mag_db)  # Convert back to Hz
plt.title("Bode Plot – Magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which='both')

# Bode Phase
plt.subplot(1, 2, 2)
plt.semilogx(w / (2 * np.pi), phase_deg)
plt.title("Bode Plot – Phase")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(True, which='both')

plt.tight_layout()
plt.show()

# --- Phasor Plot ---
plt.figure(figsize=(5, 5))
plt.plot(H_jw.real, H_jw.imag, label="Phasor Trajectory")
plt.scatter(H_jw.real[0], H_jw.imag[0], color='green', label="Low freq")
plt.scatter(H_jw.real[-1], H_jw.imag[-1], color='red', label="High freq")
plt.title("Phasor Plot of H(jω)")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
