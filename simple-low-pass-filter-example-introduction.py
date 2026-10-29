import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Create a time array
t = np.linspace(0, 1, 1000)  # 1 second duration, 1000 samples

# Create a signal: low-frequency signal + high-frequency noise
low_freq_signal = np.sin(2 * np.pi * 5 * t)  # 5 Hz component
high_freq_noise = 0.5 * np.sin(2 * np.pi * 250 * t)  # 250 Hz noise
signal = low_freq_signal + high_freq_noise

# Design a simple first-order Butterworth low-pass filter
cutoff_frequency = 20  # 20 Hz cutoff
b, a = butter(N=1, Wn=cutoff_frequency / (0.5 * 1000), btype='low')  # N=1 for first-order

# Apply the filter
filtered_signal = filtfilt(b, a, signal)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Unfiltered Signal', alpha=0.7)
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Unfiltered vs. Filtered Signal')
plt.legend()
plt.grid(True)
plt.show()
