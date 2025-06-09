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

# Define three different time constants
tau_small = period / 20    # Small time constant
tau_medium = period / 5    # Medium time constant
tau_large = period / 2     # Large time constant

# RC filter response function
def rc_response(t, tau):
    response = np.zeros_like(t)
    dt = t[1] - t[0]
    for i in range(1, len(t)):
        response[i] = response[i-1] + (dt / tau) * (input_signal[i-1] - response[i-1])
    return response

# Calculate output signals
output_small = rc_response(t, tau_small)
output_medium = rc_response(t, tau_medium)
output_large = rc_response(t, tau_large)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, input_signal, 'k--', label='Input Signal (Square Wave)')
plt.plot(t * 1000, output_small, label='Output (Small τ)')
plt.plot(t * 1000, output_medium, label='Output (Medium τ)')
plt.plot(t * 1000, output_large, label='Output (Large τ)')

plt.title('Effect of Time Constant on Signal Shape')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
