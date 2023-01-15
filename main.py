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

from numpy import mean

import lr1Common
from iism.lr4 import calculateSecondMonteKarlo
import numpy as np
import numpy.linalg as np_lin
from matplotlib import pyplot as plt

from iism.lr5 import monteCarlo, show_3D

a_matrix = np.array([
    [1.2, -0.4, 0.3],
    [0.1, 0.7, -0.2],
    [-0.4, 0.0, 1.4]
])
f_vector = np.array([1, 2, -2])
real_result = np_lin.solve(a_matrix, f_vector)
print("Решение СЛАУ")
print(real_result)

A = np.array([
    [-0.2, 0.4, -0.3],
    [-0.1, 0.3, 0.2],
    [0.4, 0.0, -0.4]
])
f = np.array([1, 2, -2])
m = 1000
N = 1000

res = monteCarlo(A=A, f=f, m=m, N=N)
print(res)

print(abs(np.array(real_result) - np.array(res)))

ox, oy, oz_1, oz_2, oz_3 = list(), list(), list(), list(), list()
# marcov_chains = [100 * i for i in range(1, 11)]
chains_length = [100 * i for i in range(1, 11)]

errors = list()
for N in chains_length:
    errorSum = 0
    print(N)
    for i in range(10):
        monteResult = monteCarlo(A=A, f=f, m=50, N=N)
        errorsVector = abs(np.array(real_result) - np.array(monteResult))
        errorSum += mean(errorsVector)
    errors.append(errorSum / 10)
    ox.append([N] * len(chains_length))

plt.plot(ox, errors, marker=".", color="green")
plt.show()

# for m in marcov_chains:
#     result_x, result_y, result_z = list(), list(), list()
#     for N in marcov_chains:
#         monte_result = monteCarlo(A=A, f=f, m=m, N=N)
#         solution_vector = abs(np.array(real_result) - np.array(monte_result))
#         # print(m, N, solution_vector)
#         result_x.append(solution_vector[0])
#         result_y.append(solution_vector[1])
#         result_z.append(solution_vector[2])
#
#     ox.append([m] * len(marcov_chains))
#     oy.append(marcov_chains)
#     oz_1.append(result_x)
#     oz_2.append(result_y)
#     oz_3.append(result_z)
#
# show_3D(ox, oy, oz_1)`
# # show_3D(ox, oy, oz_2)
# # show_3D(ox, oy, oz_3)
