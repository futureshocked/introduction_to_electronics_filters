import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 5, 1000)          # 0 to 5 ms

# Parameters
tau = 1 # Time constant in milliseconds
impulse_time = 2 # Impulse occurs at 2 ms
impulse_magnitude = 1000

# Create input impulse signal
input_impulse = np.zeros_like(t)
input_impulse[np.argmin(np.abs(t - impulse_time))] = impulse_magnitude

# Create impulse response: zero before impulse_time, then exponential decay
impulse_response = np.zeros_like(t)
impulse_response[t >= impulse_time] = impulse_magnitude * np.exp(-(t[t >= impulse_time] - impulse_time) / tau)

# Plot
plt.figure(figsize=(6, 4))
plt.plot(t, impulse_response, label='Impulse Response h(t)', color='blue')
plt.plot(t, input_impulse, label='Input Impulse', color='red', linestyle='--')
plt.axvline(x=impulse_time, color='red', linestyle='--', alpha=0.5) # Visual marker for impulse time
plt.title('Impulse Response of RC Low-Pass Filter (Impulse at 2 ms)')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.xlim(0, 5)
plt.ylim(0, 1100)
plt.tight_layout()
plt.show()
