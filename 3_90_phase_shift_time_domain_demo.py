import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 10                  # Frequency in Hz
phi_deg = -45           # Phase shift in degrees
phi_rad = np.radians(phi_deg)  # Convert phase shift to radians
T = 1 / f               # Period of the signal

# Calculate time delay corresponding to the phase shift:
# Δt = φ_rad / (2πf)
time_delay = phi_rad / (2 * np.pi * f)

# Generate time vector covering two periods
t = np.linspace(0, 2 * T, 1000)

# Generate sine wave without phase shift
y1 = np.sin(2 * np.pi * f * t)

# Generate sine wave with phase shift
y2 = np.sin(2 * np.pi * f * t + phi_rad)

# Plot both signals
plt.figure(figsize=(8, 4))
plt.plot(t, y1, label='Original Signal')
plt.plot(t, y2, label=f'Shifted Signal ({phi_deg}°)')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Phase Shift in the Time Domain")
plt.legend()
plt.grid(True, linestyle="--")
plt.show()

# Print the time delay corresponding to the phase shift
print(f"A phase shift of {phi_deg}° corresponds to a time delay of {abs(time_delay):.4f} seconds.")
