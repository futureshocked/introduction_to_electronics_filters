import numpy as np
import matplotlib.pyplot as plt

# Create time array
t = np.linspace(0, 0.1, 1000)  # 100 milliseconds total, 1000 points

# Generate a clean switch signal (ideal press at 50 ms)
switch_clean = np.zeros_like(t)
switch_clean[t > 0.05] = 1  # Switch pressed after 50 ms

# Simulate bouncing: add random rapid fluctuations around 50–55 ms
np.random.seed(0)  # For reproducibility
bouncing = np.zeros_like(t)
bounce_indices = (t > 0.05) & (t < 0.055)
bouncing[bounce_indices] = np.random.choice([0, 1], size=np.sum(bounce_indices))

# Create the bouncing signal
switch_bouncing = switch_clean.copy()
switch_bouncing[bounce_indices] = bouncing[bounce_indices]

# Define low-pass filter parameters
tau = 0.005  # Time constant in seconds (5 ms)
dt = t[1] - t[0]  # Time step size

# Apply digital RC low-pass filter
filtered_signal = np.zeros_like(switch_bouncing)
for i in range(1, len(t)):
    filtered_signal[i] = filtered_signal[i-1] + (dt / tau) * (switch_bouncing[i] - filtered_signal[i-1])

# Threshold the filtered signal to recover clean digital levels
debounced_signal = (filtered_signal > 0.5).astype(int)

# Plotting
plt.figure(figsize=(8, 8))

# Plot the bouncing signal
plt.subplot(3, 1, 1)
plt.plot(t * 1000, switch_bouncing, label='Bouncing Switch Signal')
plt.title('Raw Bouncing Switch Signal')
plt.ylabel('Signal Level')
plt.grid(True)

# Plot the filtered signal
plt.subplot(3, 1, 2)
plt.plot(t * 1000, filtered_signal, label='Filtered (Analog)', color='orange')
plt.title('Filtered (Analog) Signal')
plt.ylabel('Filtered Level')
plt.grid(True)

# Plot the debounced digital signal
plt.subplot(3, 1, 3)
plt.plot(t * 1000, debounced_signal, label='Debounced Digital Signal', color='green')
plt.title('Debounced (Digital) Signal After Threshold')
plt.xlabel('Time (ms)')
plt.ylabel('Signal Level')
plt.grid(True)

plt.tight_layout()
plt.show()
