import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define parameters
V_in = 5.0              # Square wave amplitude
frequency = 100         # Square wave frequency (Hz)
period = 1 / frequency  # Period of the square wave (s)
t = np.linspace(0, 3 * period, 1000)  # Time array over three periods

# Generate input square wave
input_signal = V_in * signal.square(2 * np.pi * frequency * t)

# Define two different time constants
tau_small = period / 20   # Small time constant
tau_large = period / 2    # Large time constant

# RC filter response function
def rc_response(t, tau):
    response = np.zeros_like(t)
    dt = t[1] - t[0]
    for i in range(1, len(t)):
        response[i] = response[i-1] + (dt / tau) * (input_signal[i-1] - response[i-1])
    return response

# Calculate output signals
output_small_tau = rc_response(t, tau_small)
output_large_tau = rc_response(t, tau_large)

# Plotting
plt.figure(figsize=(10, 6))

# Plot small tau response
plt.subplot(2, 1, 1)
plt.plot(t * 1000, input_signal, label='Input Signal', linestyle='--')
plt.plot(t * 1000, output_small_tau, label='Output (Small τ)')
plt.title('Square Wave Response - Small Time Constant')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)

# Plot large tau response
plt.subplot(2, 1, 2)
plt.plot(t * 1000, input_signal, label='Input Signal', linestyle='--')
plt.plot(t * 1000, output_large_tau, label='Output (Large τ)')
plt.title('Square Wave Response - Large Time Constant')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
