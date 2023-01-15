import math
import random

import numpy as np


def calculateFirstMonteKarlo(n):
    sumI = 0
    for i in range(n):
        x = 0
        for j in range(12):
            x += random.random()
        x -= 6
        sumI += math.exp(-math.pow(x, 4)) * math.sqrt(1 + math.pow(x, 4)) / \
                (1.0 / math.sqrt(2 * math.pi) * pow(math.e, -(pow(x, 2) / 2)))
    return sumI / n


def calculateSecondMonteKarlo(r1, fi1, r2, fi2, n):
    z = 0
    for i in range(n):
        r = random.uniform(r1, r2)
        phi = random.uniform(fi1, fi2)
        z += 1 / (np.power(r * np.cos(phi), 2) + np.power(r * np.sin(phi), 4))
    p = (fi2 - fi1) * (r2 - r1)
    return p * z / n
