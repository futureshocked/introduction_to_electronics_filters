import numpy as np
import matplotlib.pyplot as plt

R = 2e3
C = 100e-9

fc = 1 / (2 * np.pi * R * C)
print(f"Cutoff frequency: {fc:.2f} Hz\n")

frequencies = [200, 500, 1000, 2000, 5000, 10000]

plt.figure(figsize=(10, 8))

for i, f in enumerate(frequencies):
    T = 1 / f
    t = np.linspace(0, 2 * T, 1000)
    omega = 2 * np.pi * f
    v_in = np.sin(omega * t)
    H_mag = (omega * R * C) / np.sqrt(1 + (omega * R * C)**2)
    phi_rad = np.arctan(1 / (omega * R * C))  # Phase shift in radians
    phi_deg = np.degrees(phi_rad)            # Convert to degrees
    delta_t = phi_rad / omega                # Time delay in seconds

    print(f"Frequency: {f} Hz")
    print(f"  Phase shift: {delta_t * 1000:.4f} ms (Δt), {phi_deg:.2f}°\n")

    v_out = H_mag * np.sin(omega * t + phi_rad)
    plt.subplot(len(frequencies), 1, i + 1)
    plt.plot(t * 1000, v_in, label="Input Signal")
    plt.plot(t * 1000, v_out, label="Filtered Output")
    plt.title(f"RC High-Pass Filter Response at {f} Hz")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True, linestyle="--")
    plt.legend()

plt.tight_layout()
plt.show()
