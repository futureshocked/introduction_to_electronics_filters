import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Define Parameters ---
num_frames = 200
duration_seconds = 3  # Total animation time
fps = num_frames / duration_seconds

# Frequency range (e.g., from 10 Hz to 10,000 Hz)
frequencies = np.logspace(np.log10(10), np.log10(10000), num_frames)
magnitudes = 1 / np.sqrt(1 + (frequencies / 159)**2)  # Example based on RC filter behavior

# --- Set up the figure and axis ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, which='both', ls='--', lw=0.5)
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.set_title("Shrinking Phasor with Trace Line")

# Plot static reference circle
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', alpha=0.5)
ax.add_artist(circle)

# --- Initialize elements to update ---
phasor_line, = ax.plot([], [], 'r-', lw=2)
phasor_head, = ax.plot([], [], 'ro')
trace_line, = ax.plot([], [], 'b-', lw=1, alpha=0.6, label='Trace')
text_info = ax.text(0.05, 1.05, '', transform=ax.transAxes)

# Store trace points
trace_x = []
trace_y = []

# --- Initialization function ---
def init():
    trace_x.clear()
    trace_y.clear()
    phasor_line.set_data([], [])
    phasor_head.set_data([], [])
    trace_line.set_data([], [])
    text_info.set_text('')
    return phasor_line, phasor_head, trace_line, text_info

# --- Animation function ---
def animate(i):
    theta = 2 * np.pi * (i / num_frames)  # Rotation angle
    r = magnitudes[i]                     # Shrinking magnitude

    # Current phasor
    x = [0, r * np.cos(theta)]
    y = [0, r * np.sin(theta)]

    # Update phasor
    phasor_line.set_data(x, y)
    phasor_head.set_data([x[1]], [y[1]])

    # Update trace
    trace_x.append(x[1])
    trace_y.append(y[1])
    trace_line.set_data(trace_x, trace_y)

    # Update text
    text_info.set_text(f"Frequency: {frequencies[i]:.1f} Hz\nMagnitude: {r:.2f}")

    return phasor_line, phasor_head, trace_line, text_info

# --- Create Animation ---
ani = animation.FuncAnimation(fig, animate, frames=num_frames,
                              init_func=init, blit=False, interval=1000/fps)

plt.tight_layout()
ani.save('shrinking_phasor.gif', writer='pillow', fps=int(fps))
plt.show()
