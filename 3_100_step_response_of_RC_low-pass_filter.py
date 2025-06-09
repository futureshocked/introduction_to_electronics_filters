import numpy as np
import matplotlib.pyplot as plt
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Simulate RC Low-Pass Filter Response with Delayed Step Input")
parser.add_argument("--R", type=float, default=1e3, help="Resistor value in ohms")
parser.add_argument("--C", type=float, default=1e-6, help="Capacitance value in farads")
parser.add_argument("--V", type=float, default=5, help="Step input amplitude in volts")
parser.add_argument("--delay", type=float, default=5, help="Delay before step input in milliseconds")
args = parser.parse_args()

# Extract parameters from command-line arguments
R = args.R                # Resistance in ohms
C = args.C                # Capacitance in farads
V_in = args.V             # Step input amplitude in volts
delay_ms = args.delay     # Delay in milliseconds

# Convert delay to seconds
delay = delay_ms / 1000

# Calculate the time constant
tau = R * C

# Create a time vector covering from 0 to 5 time constants plus the delay (in seconds)
t = np.linspace(0, 5 * tau + delay, 1000)

# Convert time to milliseconds for plotting
t_ms = t * 1000

# Define the input step signal:
# It is 0 V for t < delay, and V_in for t >= delay
V_step = np.where(t < delay, 0, V_in)

# Calculate the filter's step response for the delayed step input:
# For t < delay, the output is 0; for t >= delay, V_out = V_in*(1 - exp(-(t - delay)/tau))
V_out = np.where(t < delay, 0, V_in * (1 - np.exp(-(t - delay) / tau)))

# Plot both the delayed input step signal and the filter's response
plt.figure(figsize=(8, 4))
plt.plot(t_ms, V_step, label="Input Step Signal (Delayed)", linestyle="--", color="green")
plt.plot(t_ms, V_out, label="Filtered Step Response", color="blue")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.title("RC Low-Pass Filter Step Response with 5 ms Delayed Input")
plt.legend()
plt.grid(True, linestyle="--")
plt.show()
