import numpy as np
import matplotlib.pyplot as plt

# Create time array
t = np.linspace(0, 0.1, 2000)  # 100 ms total

# Simulate full-wave rectified sine wave (e.g., after bridge rectifier)
mains_frequency = 50  # Hz
ripple_frequency = 2 * mains_frequency  # Full-wave rectified
V_peak = 12  # Peak voltage after rectification

# Rectified waveform with ideal peaks
rectified_voltage = V_peak * np.abs(np.sin(2 * np.pi * mains_frequency * t))

# Simulate capacitive filtering effect
# Simple model: envelope follows peaks but discharges linearly
C = 1000e-6  # 1000 uF
load_current = 0.1  # 100 mA
dt = t[1] - t[0]
Vc = np.zeros_like(t)
Vc[0] = rectified_voltage[0]

for i in range(1, len(t)):
    # Capacitor discharges slightly between peaks
    Vc[i] = Vc[i-1] - (load_current * dt / C)
    # If rectified voltage is higher than capacitor voltage, capacitor charges instantly
    if rectified_voltage[i] > Vc[i]:
        Vc[i] = rectified_voltage[i]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t * 1000, rectified_voltage, label='Rectified Voltage (No Filter)', alpha=0.5)
plt.plot(t * 1000, Vc, label='Filtered Voltage (with Capacitor)', linewidth=2)
plt.title('Power Supply Filtering with Capacitor')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
