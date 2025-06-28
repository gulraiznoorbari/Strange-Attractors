import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

dt = 0.01
steps = 100000
sigma = 10
rho = 28
beta = 8 / 3

x = [0.1]
y = [0.0]
z = [0.0]

start_color = "#007ACC"
end_color = "#9A8DD1"
cmap = mcolors.LinearSegmentedColormap.from_list("custom_colormap", [start_color, end_color])

plt.figure(facecolor="black")
plt.rcParams['axes.facecolor'] = 'black'
plt.xticks([])
plt.yticks([])

def lorenz(x, y, z):
    dx = sigma * (y[-1] - x[-1])
    dy = x[-1] * (rho - z[-1]) - y[-1]
    dz = x[-1] * y[-1] - beta * z[-1]

    return [dx, dy, dz]

for i in range(steps):    
    dx, dy, dz = lorenz(x, y, z)

    x_new = x[-1] + dx * dt;
    y_new = y[-1] + dy * dt;
    z_new = z[-1] + dz * dt;

    x.append(x_new)
    y.append(y_new)
    z.append(z_new)

    color_value = i / steps
    color = cmap(color_value)
    plt.plot(x_new, y_new, marker="o", markersize=0.1, color=color)

plt.grid(False)
plt.show()
