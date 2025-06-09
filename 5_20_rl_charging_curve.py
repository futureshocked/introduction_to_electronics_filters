import numpy as np
import matplotlib.pyplot as plt

# Define parameters
I_final = 2.0      # Final current in amperes
tau = 0.002        # Time constant in seconds (2 ms)
t = np.linspace(0, 5*tau, 500)  # Time array from 0 to 5 tau

# Calculate inductor current over time
I_l = I_final * (1 - np.exp(-t / tau))

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(t * 1000, I_l, label='Inductor Current IL(t)')
plt.axhline(I_final, color='gray', linestyle='--', label='Final Current')
plt.axvline(tau * 1000, color='red', linestyle=':', label='t = τ')
plt.xlabel('Time (ms)')
plt.ylabel('Current (A)')
plt.title('RL Current Rise Curve')
plt.legend()
plt.grid(True)
plt.show()
