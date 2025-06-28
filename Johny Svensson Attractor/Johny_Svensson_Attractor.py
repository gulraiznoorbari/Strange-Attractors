import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

a = 1.40
b = 1.56
c = 1.40
d = -6.56

x = [0]
y = [0]

steps = 100000

start_color = "#007ACC"
end_color = "#FF5F1F"
cmap = mcolors.LinearSegmentedColormap.from_list("custom_colormap", [start_color, end_color])

plt.figure(facecolor="black")
plt.rcParams['axes.facecolor'] = 'black'
plt.xticks([])
plt.yticks([])

def xEquation(prevXvalue, prevYvalue):
    newXvalue = d * np.sin(prevXvalue * a) - np.sin(prevYvalue * b)
    return [newXvalue]

def yEquation(prevXvalue, prevYvalue):
    newYvalue = c * np.cos(prevXvalue * a) + np.cos(prevYvalue * b)
    return [newYvalue]

for i in range(steps):
    tempX = x
    tempY = y

    x = xEquation(tempX[0], tempY[0])
    y = yEquation(tempX[0], tempY[0])

    color_value = i / steps
    color = cmap(color_value)
    plt.plot(x, y, marker="o", markersize=0.1, color=color)

plt.grid(False)
plt.show()
