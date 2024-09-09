import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random
import numpy as np
from math import sin, cos, pi

from sys import argv

_ = Axes3D  # get rid of unused import warning (it is dynamically used)

# use command line argument for population size
population_size = 1000
if len(argv) > 1:
    population_size = int(argv[1])


x_bounds = -100.0, 1e20
y_bounds = -1e20, 100.0


def f(x, y):
    return (
        0.5 + (cos(sin(abs(x**2 - y**2))) ** 2 - 0.5) / (1 + 0.001 * (x**2 + y**2)) ** 2
    )


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


# We make the chaotic map a generator
def chaotic_map(initial, update):
    yield initial
    current = update(initial)

    for _ in range(population_size - 1):
        yield current
        current = update(current)


# ---

x = np.linspace(*x_bounds, 150)
y = np.linspace(*y_bounds, 150)

fig = plt.figure()

# --- Logistic

logistic = lambda a: 4 * a * (1 - a)

# We initialize the sequences
logis_x = chaotic_map(0.30, logistic)
logis_y = chaotic_map(0.80, logistic)

lines = generate_lines(zip(logis_x, logis_y))
display_scatter(*lines)

# --- Sinusoidal

sinusoidal = lambda a: sin(a * pi)

sinus_x = chaotic_map(0.30, sinusoidal)
sinus_y = chaotic_map(0.80, sinusoidal)

lines = generate_lines(zip(sinus_x, sinus_y))
display_scatter(*lines)
