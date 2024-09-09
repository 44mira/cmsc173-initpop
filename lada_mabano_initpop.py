import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random
import numpy as np

from sys import argv

_ = Axes3D  # get rid of unused import warning (it is dynamically used)

# use command line argument for population size
population_size = 1000
if len(argv) > 1:
    population_size = int(argv[1])


x_bounds = -5.0, 5.0
y_bounds = -10.0, 10.0


def f(x, y):
    # factor out coefficients
    return sum(((a**4 - 16 * a**2 + 5 * a) / 2) for a in (x, y))


def generate_value(lb, ub, rand):
    return lb + (ub - lb) * rand


# create a countour3d map with equally spaced x and y values
# for comparison

x = np.linspace(*x_bounds, 150)
y = np.linspace(*y_bounds, 150)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax2 = plt.axes(projection="3d")
ax2.contour3D(X, Y, Z, 80, cmap="hot")


ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("f")

plt.show()  # show the figure

# ---

xline, yline, zline = [], [], []

for i in range(population_size):
    xline.append(generate_value(*x_bounds, random()))
    yline.append(generate_value(*y_bounds, random()))

    zline.append(f(xline[i], yline[i]))

xline, yline, zline = map(np.array, (xline, yline, zline))

ax1 = plt.axes(projection="3d")
ax1.scatter3D(xline, yline, zline, c=zline, cmap="hot", s=7)

ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

plt.show()  # show scatterplot
