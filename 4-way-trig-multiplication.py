#############################
## MULTIPLY ALL WAVE FORMS ##
#############################

import numpy as np 
import matplotlib.pyplot as plt

# Define the frequencies
f_sine = 3400
f_square = 1
f_triangle = 10300
f_sawtooth = 20800

# Duration and sample rate
duration = 2  # Seconds
sample_rate = 2.5 * max(f_sine, f_square, f_triangle, f_sawtooth) * 2  # Adequate sampling rate

# Create time array
x = np.linspace(0, duration, int(duration * sample_rate))

# Create all waveforms
sine_wave = np.sin(2 * np.pi * f_sine * x)
square_wave = np.sign(np.sin(2 * np.pi * f_square * x))
triangle_wave = 2/np.pi * np.arcsin(np.sin(2 * np.pi * f_triangle * x))
sawtooth_wave = 2 * (f_sawtooth * x - np.floor(0.5 + f_sawtooth * x))

# Multiply all waveforms
multiply_all = sine_wave * square_wave * triangle_wave * sawtooth_wave

# Plot just the product
plt.figure(figsize=(10, 6))
plt.plot(x, multiply_all, 'g-')
plt.title('Product of All Waveforms')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.xlim(0, 0.005)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.savefig('product_of_waveforms.png')
plt.show()
