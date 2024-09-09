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


def generate_lines(rands):
    xline, yline, zline = [], [], []

    for rand_x, rand_y in rands:
        curr_x = generate_value(*x_bounds, rand_x)
        curr_y = generate_value(*y_bounds, rand_y)

        xline.append(curr_x)
        yline.append(curr_y)

        zline.append(f(curr_x, curr_y))

    return map(np.array, (xline, yline, zline))


def display_scatter(xline, yline, zline):
    ax1 = plt.axes(projection="3d")
    ax1.scatter3D(xline, yline, zline, c=zline, cmap="hot", s=7)

    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")

    plt.show()  # show scatterplot


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

lines = generate_lines((random(), random()) for _ in range(population_size))
display_scatter(*lines)

# ---


# We make the chaotic map a generator
def logistic_chaotic_map(initial):
    update = lambda a: 4 * a * (1 - a)

    yield initial
    current = update(initial)

    for _ in range(population_size - 1):
        yield current
        current = update(current)


# We initialize the sequences
logis_x = logistic_chaotic_map(0.30)
logis_y = logistic_chaotic_map(0.80)

lines = generate_lines(zip(logis_x, logis_y))
display_scatter(*lines)
