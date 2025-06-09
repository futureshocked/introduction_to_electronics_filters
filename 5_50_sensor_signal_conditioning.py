import numpy as np
import matplotlib.pyplot as plt

# Create time array
t = np.linspace(0, 2, 1000)  # 2 seconds, 1000 points

# Generate clean slow signal (e.g., a sine wave to simulate a sensor)
clean_signal = np.sin(2 * np.pi * 1 * t)  # 1 Hz sine wave

# Add high-frequency noise
noise = 0.3 * np.random.normal(size=t.shape)
noisy_signal = clean_signal + noise

# Define low-pass filter parameters
tau = 0.05  # Time constant (in seconds)
dt = t[1] - t[0]  # Time step

# Apply simple RC low-pass filter
filtered_signal = np.zeros_like(noisy_signal)
for i in range(1, len(t)):
    filtered_signal[i] = filtered_signal[i-1] + (dt / tau) * (noisy_signal[i] - filtered_signal[i-1])

# Plotting
plt.figure(figsize=(10, 6))

# Plot noisy and filtered signals
plt.plot(t, noisy_signal, label='Noisy Sensor Signal', alpha=0.6)
plt.plot(t, filtered_signal, label='Filtered Sensor Signal', linewidth=2)
plt.plot(t, clean_signal, label='Original Clean Signal', linestyle='--', linewidth=2)

plt.title('Sensor Signal Conditioning with Digital Low-Pass Filter')
plt.xlabel('Time (s)')
plt.ylabel('Signal Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
