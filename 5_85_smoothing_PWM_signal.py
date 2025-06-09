import numpy as np
import matplotlib.pyplot as plt

# Create time array
t = np.linspace(0, 0.1, 5000)  # 100 ms total, 5000 points

# Generate PWM signal: 5V, 1 kHz, 30% duty cycle
pwm_frequency = 500  # Hz
duty_cycle = 50       # 50%
pwm_period = 1 / pwm_frequency
pwm_signal = ((t % pwm_period) < (duty_cycle / 100) * pwm_period).astype(float) * 5.0  # 5V PWM

# Define low-pass filter parameters
tau = 0.1  # Time constant (2 ms)
dt = t[1] - t[0]  # Time step

# Apply digital RC low-pass filter
filtered_signal = np.zeros_like(pwm_signal)
for i in range(1, len(t)):
    filtered_signal[i] = filtered_signal[i-1] + (dt / tau) * (pwm_signal[i] - filtered_signal[i-1])

# Plotting
plt.figure(figsize=(6, 6))

# PWM signal
plt.plot(t * 1000, pwm_signal, label='PWM Signal', alpha=0.5)

# Smoothed output
plt.plot(t * 1000, filtered_signal, label='Smoothed Output', linewidth=2)

plt.title('Analog Smoothing of a PWM Signal with a Low-Pass Filter')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
