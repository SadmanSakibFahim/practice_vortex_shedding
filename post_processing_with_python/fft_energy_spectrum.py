import numpy as np
import matplotlib.pyplot as plt
from fft_cl import freqs, magnitude

pos_mask = freqs > 0
freqs = freqs[pos_mask]
magnitude = magnitude[pos_mask]

A = np.abs(magnitude) # amplitude
E = A**2 # Energy spectrum
T = np.sum(E) # Total energy
E_frac = E / T # Fractional energy spectrum

top_E = np.argsort(E_frac)[::-1]
E_frac_max = E_frac[top_E[0]]

print(f"The top frequency contributes {E_frac_max*100:.2f}% of the total energy.")

plt.figure(figsize = (10,5))
plt.plot(freqs, E_frac, label = 'Energy Fraction')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Energy Fraction')
plt.title('Energy Spectrum of Lift Coefficient (Cl)')
plt.legend()
plt.grid(True)
plt.show()




