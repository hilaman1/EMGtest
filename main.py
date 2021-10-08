from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import mne

# A Notch Filter is a bandstop filter with a very narrow stopband and two passbands,
# it actually highly attenuates/eliminates a particular frequency component from the input
# signal while leaving the amplitude of the other frequencies more or less unchanged.

# Create/view notch filter

samp_freq = 100  # Sample frequency (Hz)
notch_freq = 50.0  # Frequency to be removed from signal (Hz)
quality_factor = 20.0  # Quality factor

# Design a notch filter using signal.iirnotch
b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)

# Compute magnitude response of the designed filter
freq, h = signal.freqz(b_notch, a_notch, fs=samp_freq)

fig = plt.figure(figsize=(8, 6))

# Plot magnitude response of the filter
plt.plot(freq * samp_freq / (2 * np.pi), 20 * np.log10(abs(h)),
         'r', label='Bandpass filter', linewidth='2')
plt.xlabel('Frequency [Hz]', fontsize=20)
plt.ylabel('Magnitude [dB]', fontsize=20)
plt.title('Notch Filter', fontsize=20)
plt.grid()
file_path = '001_0.edf'
noisySignal = mne.io.read_raw_edf(file_path, preload=True)

# Plotting
fig = plt.figure(figsize=(8, 6))
plt.subplot(211)
plt.plot(n, noisySignal, color='r', linewidth=2)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Magnitude', fontsize=18)
plt.title('Noisy Signal', fontsize=20)

# Apply notch filter to the noisy signal using signal.filtfilt
outputSignal = signal.filtfilt(b_notch, a_notch, noisySignal)

# Plot notch-filtered version of signal
plt.subplot(212)

# Plot output signal of notch filter
plt.plot(n, outputSignal)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Magnitude', fontsize=18)
plt.title('Filtered Signal', fontsize=20)
plt.subplots_adjust(hspace=0.5)
fig.tight_layout()
plt.show()
