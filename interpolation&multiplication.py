import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#Sine Wave Parameters
f_sine = 1 # Frequency of the Sine Wave
duration_sine = 2 # Secounds
sample_rate_sine = 1000 # Samples per Secound

# Parameters for the Square Wave (Different Time Dimensions)
f_square = 2 # Frequency for Square Wave (Hz)
duration_square = 3 # Different Duration
sample_rate_square = 1500 # Different Sample Rate Than Sine

# Create Individual time Arrays for Sine and Square
x_sine = np.linspace(0, duration_sine, duration_sine * sample_rate)
x_square = np.linspace(0, duration_square, duration_square * sample_rate)

# Create the WaveForms
sine_wave = np.sin(2 * np.pi * f_sine * x_sine)
square_wave_og = np.sign(np.sin(2 * np.pi * f_square * x_square))

# Interpolation Function for Matching the Sine Wave's Square Function
square_interpolator = interpolate.interp1d(
    x_square, 
    square_wave_og,
    kind='nearest',
    bounds_error=False,
    fill_value=0 
)

# Resampled wave matches the sine waves time points:
square_wave_resample = square_interpolator(x_sine)

# Now Multiply
multi1 = sine_wave * square_wave_resample

# Create Plots

###############
## SINE WAVE ##
###############

plt.figure(figsize=(10, 6))
plt.plot(x_sine, sine_wave, 'b-')
plt.title(f'Sine Wave (f = {f_sine} Hz, duration = {duration_sine}s)')
plt.xlabel('Time(Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.savefig('sinewave.png')
plt.show()

###############################################
## ORIGINAL SQUARE WAVE -- PRE-INTERPOLATION ##
###############################################

plt.figure(figsize=(10, 6))
plt.plot(x_square, square_wave_og, 'r-')
plt.title(f'Original Square Wave (f = {f_square} Hz, duration = {duration_square}s)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.savefig('original_square_wave.png')
plt.show()

#################################################
## RESAMPLED SQUARE WAVE -- POST-INTERPOLATION ##
#################################################

plt.figure(figsize=(10, 6))
plt.plot(x_sine, square_wave_resample, 'r--')
plt.title(f'Resampled Square')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.savefig('resampled_squarewave.png')
plt.show()

########################################################
## SINE WAVE MULTIPLIED BY THE RE-SAMPLED SQUARE WAVE ##
########################################################

plt.figure(figsize=(10, 6))
plt.plot(x_sine, multi1, 'g-')
plt.title(f'Sine * Square Waveform')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.savefig('sine_times_square.png')
plt.show()
