import random

import numpy as np


def normalDistribution(n=1000, m=-5, s2=25):
    distr = [0] * n
    for i in range(n):
        temp = 0
        for j in range(12):
            temp += random.random()
        temp -= 6
        distr[i] = m + np.sqrt(s2) * temp
    return distr


def laplasDistribution(n=1000, a=1):
    distr = [0] * n
    for i in range(n):
        temp = random.random()
        if temp < 0.5:
            distr[i] = (1 / a) * np.log(2 * temp)
        else:
            distr[i] = (-1 / a) * np.log(2 * (1 - temp))
    return distr


def exponentialDistribution(n=1000, a=4):
    distr = []
    for i in range(n):
        distr.append(-1 / a * np.log(random.random()))
    return distr

