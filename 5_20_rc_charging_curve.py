import numpy as np
import matplotlib.pyplot as plt

# Define parameters
V_in = 5.0         # Step input voltage in volts
tau = 0.001        # Time constant in seconds (1 ms)
t = np.linspace(0, 5*tau, 500)  # Time array from 0 to 5 tau

# Calculate capacitor voltage over time
V_c = V_in * (1 - np.exp(-t / tau))

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(t * 1000, V_c, label='Capacitor Voltage Vc(t)')
plt.axhline(V_in, color='gray', linestyle='--', label='Final Voltage')
plt.axvline(tau * 1000, color='red', linestyle=':', label='t = τ')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.title('RC Charging Curve')
plt.legend()
plt.grid(True)
plt.show()
