import matplotlib.pyplot as plt
print("Running")

time = [0, 1, 2, 3, 4]
position = [0, 100, 200, 300, 250]

plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
