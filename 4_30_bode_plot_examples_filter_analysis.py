import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_bode(system, f_c, title_prefix, f_range=(10, 1e6), slope=None, annotate_phase=True):
    w = 2 * np.pi * np.logspace(np.log10(f_range[0]), np.log10(f_range[1]), 1000)
    w, mag, phase = signal.bode(system, w)

    f_c_index = np.argmin(np.abs(w / (2 * np.pi) - f_c))

    # Magnitude plot
    plt.figure()
    plt.semilogx(w / (2 * np.pi), mag)
    plt.axvline(f_c, color='red', linestyle='--', label=f"Cutoff = {f_c:.1f} Hz")
    plt.scatter([f_c], [mag[f_c_index]], color='red')
    if slope:
        slope_freqs = np.array([f_c, f_c * 10])
        slope_mags = np.array([mag[f_c_index], mag[f_c_index] + slope])
        plt.semilogx(slope_freqs, slope_mags, 'k--', label=f"{slope:+} dB/decade")
    plt.title(f"{title_prefix} - Magnitude")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.legend()
    plt.grid(True)

    # Phase plot
    plt.figure()
    plt.semilogx(w / (2 * np.pi), phase)
    plt.axvline(f_c, color='red', linestyle='--', label=f"Cutoff = {f_c:.1f} Hz")
    plt.scatter([f_c], [phase[f_c_index]], color='red')
    plt.title(f"{title_prefix} - Phase")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (degrees)")
    plt.legend()
    plt.grid(True)

# RC Filter
R_rc = 10e3
C_rc = 10e-9
f_c_rc = 1 / (2 * np.pi * R_rc * C_rc)
num_rc = [1]
den_rc = [R_rc * C_rc, 1]
system_rc = signal.TransferFunction(num_rc, den_rc)
plot_bode(system_rc, f_c_rc, "RC Low-Pass Filter", slope=-20)

# RL Filter
R_rl = 1e3
L_rl = 10e-3
f_c_rl = R_rl / (2 * np.pi * L_rl)
num_rl = [L_rl, 0]
den_rl = [L_rl, R_rl]
system_rl = signal.TransferFunction(num_rl, den_rl)
plot_bode(system_rl, f_c_rl, "RL High-Pass Filter", slope=20)

plt.show()
