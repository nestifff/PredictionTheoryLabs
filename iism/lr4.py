import math
import random


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
