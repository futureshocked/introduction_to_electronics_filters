import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the CSV and skip header lines starting with '#'
df = pd.read_csv("rc_low_pass_analyser_data.csv", comment='#')

# Extract data from relevant columns
frequencies = df["Frequency (Hz)"]
magnitudes_db = df["Channel 2 Magnitude (dB)"]
phases_deg = df["Channel 2 Phase (deg)"]

# Convert dB to linear magnitude
magnitudes = 10 ** (magnitudes_db / 20)
phases_rad = np.radians(phases_deg)

# Convert magnitude and phase to complex phasors
phasors = magnitudes * np.exp(1j * phases_rad)
real_parts = np.real(phasors)
imag_parts = np.imag(phasors)

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 6))
fig.subplots_adjust(top=0.82)  # Make room above the plot
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.grid(True, linestyle='--')
ax.set_title("Phasor Animation (Measured)", pad=20)

# Initialize animated elements
line, = ax.plot([], [], 'r-', lw=2)  # Current phasor
point, = ax.plot([], [], 'ro')       # Phasor tip
trace, = ax.plot([], [], 'b--', lw=1)  # Trace connecting tips

# Label positioned in figure space above the plot
label = fig.text(0.5, 0.93, '', ha='center', va='top', fontsize=10,
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Store the trace points
trace_x, trace_y = [], []

def init():
    line.set_data([], [])
    point.set_data([], [])
    trace.set_data([], [])
    label.set_text('')
    trace_x.clear()
    trace_y.clear()
    return line, point, trace, label

def animate(i):
    x = real_parts[i]
    y = imag_parts[i]

    # Update phasor line and point
    line.set_data([0, x], [0, y])
    point.set_data([x], [y])

    # Append new point to trace and update trace line
    trace_x.append(x)
    trace_y.append(y)
    trace.set_data(trace_x, trace_y)

    # Update label text above the title
    label.set_text(f"f = {frequencies[i]:.0f} Hz   |H| = {magnitudes[i]:.2f}   ∠ = {phases_deg[i]:.1f}°")

    return line, point, trace, label

ani = animation.FuncAnimation(fig, animate, frames=len(frequencies),
                              init_func=init, blit=False, interval=200)

plt.show()
