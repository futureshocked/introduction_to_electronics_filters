import numpy as np
import matplotlib.pyplot as plt
import argparse

# Set up argument parsing for flexibility
parser = argparse.ArgumentParser(description="Simulate Impulse Response of an RC Low-Pass Filter")
parser.add_argument("--R", type=float, default=1e3, help="Resistor value in ohms")
parser.add_argument("--C", type=float, default=1e-6, help="Capacitance value in farads")
args = parser.parse_args()

# Extract component values
R = args.R      # Resistance in ohms
C = args.C      # Capacitance in farads

# Calculate the time constant
tau = R * C

# Create a time vector from 0 to 5 time constants (in seconds)
t = np.linspace(0, 5 * tau, 1000)

# Calculate the impulse response for an RC low-pass filter: h(t) = (1/(RC)) * exp(-t/(RC))
h_t = (1 / (R * C)) * np.exp(-t / (R * C))

# Convert time to milliseconds for plotting
t_ms = t * 1e3

# Plot the impulse response
plt.figure(figsize=(8, 4))
plt.plot(t_ms, h_t, label="Impulse Response h(t)")

# Plot a vertical red dashed line at time = 0 to represent the input impulse
plt.axvline(x=0, color="red", linestyle="--", label="Input Impulse")

plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.title("Impulse Response of RC Low-Pass Filter")
plt.grid(True, linestyle="--")
plt.legend()
plt.show()
