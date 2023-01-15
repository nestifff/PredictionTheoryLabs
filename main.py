# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# lr1Common.showLr1_2()
# lr1Common.showLr1_1()

# distr = lr2.negBinomialDistribution(m=4, p=0.2, n=1000)
# lr2.pearsonNegBinomial(n=1000, m=4, p=0.2, distr=distr)
#
# distr2 = lr2.geometricDistribution(p=0.5, n=1000)
# lr2.pearsonGeometric(n=1000, p=0.5, distr=distr)

# iism.common.plotValuesList(distr2)
import math

from iism.lr4 import calculateSecondMonteKarlo
import numpy as np
from matplotlib import pyplot as plt

#
#
# res = 2.87001
# resExp = calculateSecondMonteKarlo(r1=1, fi1=0, r2=2, fi2=2 * np.pi, n=1000)
# print(resExp)
# print(res - resExp)

ansSecond = 2.87001
n = 10000
errors = []
indices = list(range(n // 100))
indices = [x * 100 for x in indices]
for i in range(10, n+1, 100):
    res = calculateSecondMonteKarlo(r1=1, fi1=0, r2=2, fi2=2 * np.pi, n=i)
    error = math.fabs(ansSecond - res) / ansSecond
    errors.append(error)
plt.plot(indices, errors, marker=".", color="blue")
plt.legend()
plt.grid(True)
plt.show()
