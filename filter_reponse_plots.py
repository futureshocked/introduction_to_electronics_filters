import numpy as np
import matplotlib.pyplot as plt

def plot_filters():
    # Frequency range (logarithmic)
    freq = np.logspace(0, 5, 500)  # 1 Hz to 100 kHz

    # Define cutoff frequencies
    f_low_cutoff = 1000  # 1 kHz
    f_high_cutoff = 10000  # 10 kHz

    # Angular frequencies
    omega = 2 * np.pi * freq
    omega_low = 2 * np.pi * f_low_cutoff
    omega_high = 2 * np.pi * f_high_cutoff

    # First-order transfer functions (magnitude)
    low_pass = 1 / np.sqrt(1 + (freq / f_low_cutoff)**2)
    high_pass = (freq / f_low_cutoff) / np.sqrt(1 + (freq / f_low_cutoff)**2)

    # Band-pass and Band-stop approximations
    band_pass = (freq / f_low_cutoff) / np.sqrt((1 + (freq / f_low_cutoff)**2)*(1 + (freq / f_high_cutoff)**2))
    band_stop = np.sqrt((1 + (freq / f_low_cutoff)**2) / (1 + (freq / f_high_cutoff)**2))

    # Create plots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    axs[0, 0].semilogx(freq, 20*np.log10(low_pass))
    axs[0, 0].set_title('Low-Pass Filter')
    axs[0, 0].set_xlabel('Frequency (Hz)')
    axs[0, 0].set_ylabel('Magnitude (dB)')
    axs[0, 0].grid(True, which='both', ls='--')

    axs[0, 1].semilogx(freq, 20*np.log10(high_pass))
    axs[0, 1].set_title('High-Pass Filter')
    axs[0, 1].set_xlabel('Frequency (Hz)')
    axs[0, 1].set_ylabel('Magnitude (dB)')
    axs[0, 1].grid(True, which='both', ls='--')

    axs[1, 0].semilogx(freq, 20*np.log10(band_pass))
    axs[1, 0].set_title('Band-Pass Filter')
    axs[1, 0].set_xlabel('Frequency (Hz)')
    axs[1, 0].set_ylabel('Magnitude (dB)')
    axs[1, 0].grid(True, which='both', ls='--')

    axs[1, 1].semilogx(freq, 20*np.log10(band_stop))
    axs[1, 1].set_title('Band-Stop Filter')
    axs[1, 1].set_xlabel('Frequency (Hz)')
    axs[1, 1].set_ylabel('Magnitude (dB)')
    axs[1, 1].grid(True, which='both', ls='--')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_filters()
