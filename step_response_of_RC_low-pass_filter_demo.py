import numpy as np
import matplotlib.pyplot as plt

# Define filter parameters
R = 1e3       # Resistance in ohms
C = 1e-6      # Capacitance in farads
V_in = 5      # Step input voltage in volts

# Calculate the time constant
tau = R * C

# Create a time vector over 5 time constants (in seconds)
t = np.linspace(0, 5 * tau, 1000)

# Calculate the step response of an RC low-pass filter
V_out = V_in * (1 - np.exp(-t / tau))

# Convert time to milliseconds for plotting
t_ms = t * 1e3

# Plot the step response
plt.figure(figsize=(8, 4))
plt.plot(t_ms, V_out, label="Step Response")
plt.xlabel("Time (ms)")
plt.ylabel("Output Voltage (V)")
plt.title("RC Low-Pass Filter Step Response")
plt.grid(True, linestyle="--")
plt.legend()
plt.show()
