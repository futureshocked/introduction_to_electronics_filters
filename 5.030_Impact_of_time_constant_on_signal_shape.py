import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Define parameters
V_in = 5.0
frequency = 100  # Hz
period = 1 / frequency
t = np.linspace(0, 3 * period, 1000)
input_signal = V_in * signal.square(2 * np.pi * frequency * t)

# RC response function
def rc_response(t, tau):
    response = np.zeros_like(t)
    dt = t[1] - t[0]
    for i in range(1, len(t)):
        response[i] = response[i-1] + (dt / tau) * (input_signal[i-1] - response[i-1])
    return response

# Time constants
tau_small = period / 20
tau_large = period / 2

# --- First Plot: Small time constant ---
response_small = rc_response(t, tau_small)
plt.figure(figsize=(10, 6))
plt.plot(t, input_signal, label='Input (Square Wave)')
plt.plot(t, response_small, label=f'RC Output (τ = {tau_small:.4f} s)')
plt.title('RC Filter Response – Small Time Constant')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.savefig('rc_filter_small_tau.png', dpi=300, bbox_inches='tight')

# --- Second Plot: Large time constant ---
response_large = rc_response(t, tau_large)
plt.figure(figsize=(10, 6))
plt.plot(t, input_signal, label='Input (Square Wave)')
plt.plot(t, response_large, label=f'RC Output (τ = {tau_large:.4f} s)')
plt.title('RC Filter Response – Large Time Constant')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.savefig('rc_filter_large_tau.png', dpi=300, bbox_inches='tight')
