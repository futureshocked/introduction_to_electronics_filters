
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
A = 1.0             # amplitude
f = 1.0             # frequency in Hz
omega = 2 * np.pi * f
phi = np.pi / 6     # phase shift in radians (30 degrees)
duration = 2        # seconds
fps = 30
frames = int(duration * fps)
t = np.linspace(0, duration, frames)

# Set up the figure and axes
fig, (ax_phasor, ax_wave) = plt.subplots(1, 2, figsize=(10, 4))

# --- Phasor plot setup ---
ax_phasor.set_xlim(-A*1.2, A*1.2)
ax_phasor.set_ylim(-A*1.2, A*1.2)
ax_phasor.set_aspect('equal')
ax_phasor.grid(True, linestyle='--')
ax_phasor.set_title("Phasor (Complex Plane)")
phasor_line, = ax_phasor.plot([], [], 'r-', lw=2)
phasor_point, = ax_phasor.plot([], [], 'ro')

# --- Wave plot setup ---
ax_wave.set_xlim(0, duration)
ax_wave.set_ylim(-A*1.2, A*1.2)
ax_wave.grid(True, linestyle='--')
ax_wave.set_title("Sine Wave (Real Part)")
wave_line, = ax_wave.plot([], [], 'b-', lw=2)
wave_dot, = ax_wave.plot([], [], 'bo')

# Pre-allocate wave array
wave_y = np.zeros(frames)

def init():
    phasor_line.set_data([], [])
    phasor_point.set_data([], [])
    wave_line.set_data([], [])
    wave_dot.set_data([], [])
    return phasor_line, phasor_point, wave_line, wave_dot

def animate(i):
    t_now = t[i]
    
    # Phasor
    x = A * np.cos(omega * t_now + phi)
    y = A * np.sin(omega * t_now + phi)
    phasor_line.set_data([0, x], [0, y])
    phasor_point.set_data([x], [y])
    
    # Sine wave
    wave_y[i] = x
    wave_line.set_data(t[:i+1], wave_y[:i+1])
    wave_dot.set_data([t_now], [x])
    
    return phasor_line, phasor_point, wave_line, wave_dot

ani = animation.FuncAnimation(fig, animate, frames=frames,
                              init_func=init, blit=True, interval=1000/fps)

plt.tight_layout()
plt.show()
