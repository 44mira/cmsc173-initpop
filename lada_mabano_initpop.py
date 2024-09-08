import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from random import random
import numpy as np

population_size = 1000

lb_x, ub_x = -5.0, 5.0
lb_y, ub_y = -10.0, 10.0


def f(x, y):
    # factor out coefficients
    return sum(((a**4 - 16 * a**2 + 5 * a) / 2) for a in (x, y))


def generate_value(lb, ub):
    return lb + (ub - lb) * random()
