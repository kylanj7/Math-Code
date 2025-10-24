############################
# Import Required packages #
############################

import numpy as np 
import matplotlib.pyplot as plt

###########################################
# Define the parameters for yor Sine Wave #
###########################################

f1 = 2 # Frequency of the Sine Wave
duration1 = 1 # Secounds
sample_rate1 = 10000 # Samples per. Secound

# Create a Time Array
x1 = np.linspace(0, duration1, duration1 * sample_rate1)

# Sine Wave Formula
sine_wave = np.sin(2 * np.pi * f * x1)

#############################################
# Define the paramters for your Square Wave #
#############################################

f2 = 1
duration2 = 2
sample_rate2 = 10000

# Create the Time Array
x2 = np.linspace(0, duration2, duration2 * sample_rate2)

# Square Wave Formula 
square_wave = np.sign(np.sin(2 * np.pi * f2 * x2))

###############################################
# Define the paramters for your Triangle Wave #
###############################################

f3 = 1
duration3 = 2
sample_rate3 = 10000

# Create the Time Array
x3 = np.linspace(0, duration3, duration3 * sample_rate3)

# Triangle Wave Formula
triangle_wave = np.arcsin(np.sin(np.pi * f3 * x3))

###############################################
# Define the paramters for your Sawtooth Wave #
###############################################

f4 = 1
duration4 = 2
sample_rate4 = 10000

# Create the Time Array
x4 = np.linspace(0, duration4, duration4 * sample_rate4)

# Sawtooth Wave Formula
sawtooth_wave = np.mod(f4 * x4, 1)* 2 -1

###################################
# Create a Plot for the Sine Wave #
###################################

plt.figure(figsize=(10, 6))
plt.plot(x1, sine_wave)
plt.title('Sine Wave')
plt.xlabel('Sine Wave')
plt.ylabel('Time Secounds')
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.savefig('sine_wave.png')
plt.show()

#####################################
# Create a Plot for the Square Wave #
#####################################

plt.figure(figsize=(10, 6))
plt.plot(x2, square_wave, 'r-')
plt.title('Square Wave')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.2, 1.2)
plt.savefig('square_wave.png')
plt.show()

#######################################
# Create a Plot for the Triangle Wave #
#######################################

plt.figure(figsize=(10, 6))
plt.plot(x3, triangle_wave, 'r-')
plt.title('Triangle Wave')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.7, 1.7)
plt.savefig('square_wave.png')
plt.show()

#######################################
# Create a Plot for the Sawtooth Wave #
#######################################

plt.figure(figsize=(10, 6))
plt.plot(x4, sawtooth_wave, 'r-')
plt.title('Sawtooth Wave')
plt.xlabel('Time (Sec)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.2, 1.2)
plt.savefig('square_wave.png')
plt.show()
