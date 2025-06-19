import numpy as np
import matplotlib.pyplot as plt

# data loading
data = np.loadtxt("cl_vs_time.txt", skiprows = 0)

# assign columns
time = data[:, 2]
cl = data[:, 1]

# detrending
cl_detrended = cl - np.mean(cl)

# time step and sampling frequency
dt = time[1] - time[0]
Fs = 1 / dt 

# sample number
n = len(cl_detrended)

# FFT
cl_fft = np.fft.fft(cl_detrended)
freqs = np.fft.fftfreq(n, d = dt)

# halving positive frequencies
half_n = n // 2
magnitude = np.abs(cl_fft[:half_n])
freqs = freqs[:half_n]

# finding peak shedding freq
peak_index = np.argmax(magnitude)
f_shedding = freqs[peak_index]
second_peak = np.argmax(magnitude - f_shedding)
f_shedding_2 = freqs[second_peak]

# strouhal number analysis
Dia = 0.05 # meters
U = 100 # m/s
St = f_shedding * Dia / U 

# results
print(f"Time step (dt): {dt:.6e} s")
print(f"Shedding Frequency: {f_shedding:.2f} Hz")
print(f"Estimated Strouhal number: {St:.4f}")
print(f"Second Shedding Frequency: {f_shedding_2:.2f} Hz")

# Plotting FFT
plt.figure(figsize = (10, 5))
plt.plot(freqs, magnitude, color = 'blue')
plt.title("FFT of Lift Coefficient (Cl)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()