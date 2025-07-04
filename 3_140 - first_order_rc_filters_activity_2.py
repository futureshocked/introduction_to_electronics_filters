import numpy as np
import matplotlib.pyplot as plt

# Define circuit parameters
R = 1e3      # Resistance in ohms
C = 1e-6     # Capacitance in farads

# Calculate the cutoff frequency
fc = 1 / (2 * np.pi * R * C)

# Define frequencies for simulation
frequencies = [10, fc, 100e3]  # 10 Hz, cutoff frequency, 100 kHz

# Time vector parameters
# For each frequency, we simulate over two periods
plt.figure(figsize=(10, 8))

for i, f in enumerate(frequencies):
    T = 1 / f  # period of the sine wave
    t = np.linspace(0, 2 * T, 1000)  # time vector over two periods

    # Angular frequency
    omega = 2 * np.pi * f

    # Input sine wave
    v_in = np.sin(omega * t)

    # Calculate magnitude and phase shift for the filter response
    H_mag = 1 / np.sqrt(1 + (omega * R * C)**2)
    phi = -np.arctan(omega * R * C)

    # Output sine wave (filtered signal)
    v_out = H_mag * np.sin(omega * t + phi)

    # Plot input and output waveforms
    plt.subplot(len(frequencies), 1, i + 1)
    plt.plot(t, v_in, label="Input Signal")
    plt.plot(t, v_out, label="Filtered Output")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"Sinusoidal Response at f = {f:.2f} Hz")
    plt.legend()
    plt.grid(True, linestyle="--")

plt.tight_layout()
plt.show()
