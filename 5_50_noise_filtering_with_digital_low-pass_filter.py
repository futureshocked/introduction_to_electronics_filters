import numpy as np
import matplotlib.pyplot as plt

# Create time array
t = np.linspace(0, 2, 2000)  # 2 seconds, 2000 points

# Generate a slow clean signal (e.g., 1 Hz sine wave)
clean_signal = np.sin(2 * np.pi * 1 * t)

# Add high-frequency noise (simulate 50 Hz noise + random spikes)
power_line_noise = 0.2 * np.sin(2 * np.pi * 50 * t)  # 50 Hz hum
random_noise = 0.1 * np.random.normal(size=t.shape)
noisy_signal = clean_signal + power_line_noise + random_noise

# Define low-pass filter parameters
tau = 0.02  # Time constant in seconds
dt = t[1] - t[0]  # Time step size

# Apply simple RC low-pass filter
filtered_signal = np.zeros_like(noisy_signal)
for i in range(1, len(t)):
    filtered_signal[i] = filtered_signal[i-1] + (dt / tau) * (noisy_signal[i] - filtered_signal[i-1])

# Plotting
plt.figure(figsize=(12, 6))

# Plot noisy and filtered signals
plt.plot(t, noisy_signal, label='Noisy Signal', alpha=0.5)
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.plot(t, clean_signal, '--', label='Original Clean Signal', linewidth=2)

plt.title('Noise Filtering with a Digital RC Low-Pass Filter')
plt.xlabel('Time (s)')
plt.ylabel('Signal Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
