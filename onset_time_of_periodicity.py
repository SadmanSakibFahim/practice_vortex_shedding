import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("cl_vs_time.txt")
time = data[:, 2]
cl = data[:, 1]

dt = time[1] - time[0]
window_size = min(200, int(0.05/dt))

cl_rms = []
time_rms = []

for i in range(len(cl) - window_size):
    window = cl[i: i+window_size]
    rms =np.sqrt(np.mean((window - np.mean(window))**2))
    cl_rms.append(rms)
    time_rms.append(time[i + window_size//2])

plt.figure(figsize = (10, 5))
plt.plot(time_rms, cl_rms, label = 'Onset Time of Periodicity', color = 'blue')
plt.xlabel("Time (s)")
plt.ylabel("RMS of Lift Coefficient w(Cl)")
plt.grid(True)
plt.show()

# the plot shows the onset time of periodicity in the lift coefficient.
# for normal vortex shedding, the plot should have a ramp-up phase 
# which indicates gradual increase in the strength of the vortices.
# the plateau reached at the top signifies the steady state of periodic vortex shedding
# with constant vortex strength. However, the plot generated here shows a ramp-up phase, 
# followed by ramp-down phase. the likely cause of this observation is that the domain of
# the simulation is bounded at the top and the bottom with no slip walls. 
# this causes the vortices to be shed from the top and bottom walls.