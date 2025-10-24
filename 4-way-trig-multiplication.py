############################
# Import Required packages #
############################

import numpy as np 
import matplotlib.pyplot as plt

############################################################
## Create a Time Array for all of our Existing Wave Forms ##
############################################################

x = np.linspace(0, duration1, duration1 * sample_rate1)

##############################################
## Define the parameters for your Waveforms ##
##############################################

# Sine Wave Parameters #
f_sine = 3400 # Frequency of the Sine Wave
duration_sine = 2 # Secounds
sample_rate_sine = 10000 # Samples per. Secound

# Square Wave Parameters #
f_square = 1
duration_square = 2
sample_rate_square = 10000

# Triangle Wave Parameters #
f_triangle = 10300
duration_triangle = 2
sample_rate_triangle = 10000

# Sawtooth Wave Parameters #
f_sawtooth = 20800
duration_sawtooth = 2
sample_rate_sawtooth = 10000

############################################
## Define the Functions of our Wave Forms ##
############################################

# Sine Wave Formula
sine_wave = np.sin(2 * np.pi * f_sine * x)

# Square Wave Formula
square_wave = np.sign(np.sin(2 * np.pi * f_square * x))

# Triangle Wave Formula
triangle_wave = 2/np.pi * np.arcsin(np.sin(2 * np.pi * f_triangle * x))

# Sawtooth Wave Formula
sawtooth_wave = 2 * (f_sawtooth * x - np.floor(0.5 + f_sawtooth * x))

# Multiply all waveforms
multiply_all = sine_wave * square_wave * triangle_wave * sawtooth_wave

##########################################
# Create a Plots for the Wave Parameters #
##########################################

plt.figure(figsize=(10, 6))
plt.plot(x, multiply_all, 'g-')
plt.title(f'Sine * Square Waveform')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(0.01, 0.05)
plt.savefig('sine_times_square.png')
plt.show()
