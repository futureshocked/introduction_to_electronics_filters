import numpy as np
import matplotlib.pyplot as plt
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Simulate RL Low-Pass Filter Response")
parser.add_argument("--R", type=float, required=True, help="Resistor value in ohms")
parser.add_argument("--L", type=float, required=True, help="Inductor value in henrys")
parser.add_argument("--f", type=float, required=True, help="Input signal frequency in Hz")
parser.add_argument("--V", type=float, required=True, help="Input signal amplitude in volts")
args = parser.parse_args()

# Extract parameters from command-line arguments
R = args.R      # Resistance in ohms
L = args.L      # Inductance in henrys
f = args.f      # Frequency in Hz
V_in_amp = args.V  # Input amplitude in volts

# Angular frequency
omega = 2 * np.pi * f

# Calculate filter response parameters for an RL low-pass filter
H_mag = R / np.sqrt(R**2 + (omega * L)**2)
phi = -np.arctan(omega * L / R)  # Phase shift in radians

# Display calculated amplitude scaling and phase shift (in degrees)
print(f"Calculated amplitude scaling: {H_mag:.3f}")
print(f"Calculated phase shift: {np.degrees(phi):.2f} degrees")

# Generate time vector for two periods of the input signal (in seconds)
T = 1 / f
t = np.linspace(0, 2 * T, 1000)

# Convert time vector to milliseconds for plotting
t_ms = t * 1000

# Create input and output signals
v_in = V_in_amp * np.sin(omega * t)
v_out = V_in_amp * H_mag * np.sin(omega * t + phi)

# Plot the input and output waveforms
plt.figure(figsize=(8, 4))
plt.plot(t_ms, v_in, label="Input Signal")
plt.plot(t_ms, v_out, label="Output Signal")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude (V)")
plt.title("RL Low-Pass Filter Response")
plt.legend()
plt.grid(True, linestyle="--")

# Add a text box with the calculated values
textstr = f"Amplitude Scaling: {H_mag:.3f}\nPhase Shift: {np.degrees(phi):.2f}°"
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

plt.show()
