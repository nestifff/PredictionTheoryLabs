import random
import random
import numpy as np
import numpy.linalg as np_lin
import matplotlib.pyplot as mth_p
from mpl_toolkits.mplot3d import Axes3D


def monteCarlo(A, f, m, N):
    pi = [1 / len(A)] * len(A)
    p = [pi] * 3
    res = list()
    for i in range(3):
        h = [0, 0, 0]
        h[i] = 1
        ksi = [0] * m
        for j in range(m):
            currList = list()
            for k in range(N + 1):
                alpha = random.random()
                for ind in range(len(pi)):
                    if alpha < sum(pi[:ind + 1]):
                        currList.append(ind)
                        break
            if pi[currList[0]] > 0:
                Q = [h[currList[0]] / pi[currList[0]]]
            else:
                Q = [0]
            for k in range(1, N + 1):
                if p[currList[k - 1]][currList[k]] > 0:
                    temp = Q[k - 1] * A[currList[k - 1]][currList[k]] / p[currList[k - 1]][currList[k]]
                else:
                    temp = 0
                Q.append(temp)
            for k in range(N + 1):
                ksi[j] += Q[k] * f[currList[k]]
        x = sum(ksi) / m
        res.append(x)
    return res


def show_3D(ox, oy, oz):
    fig = mth_p.figure()
    axes = Axes3D(fig)
    axes.set_xlabel('Количество цепей')
    axes.set_ylabel('Длина цепи')
    axes.set_zlabel('Погрешность')
    axes.scatter3D(np.array(ox), np.array(oy), np.array(oz))
    mth_p.show()
