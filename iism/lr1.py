import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt


def linearCongruentMethod(n=1000, b=24389, a0=24398, c=0, M=2 ** 31):
    aCurr = a0
    sequence = []
    for t in range(n):
        aCurr = (b * aCurr + c) % M
        sequence.append(aCurr / M)
    return sequence


def macLarenMarsagliaMethod(n=1000, K=32):
    bi = linearCongruentMethod(n=n)
    ci = linearCongruentMethod(n=n, b=262147, a0=262147)
    V = bi[0:K]
    sequence = []
    for t in range(n):
        s = int(ci[t] * K)
        sequence.append(V[s])
        V[s] = bi[(t + K) % n]
    return sequence


def pearsonTestUniform(values):
    n = len(values)
    L = 10
    counts = np.histogram(values, bins=np.arange(0, 1 + 1 / L, 1 / L))[0]
    xi2 = np.sum((counts - n / L) ** 2 / (n / L))
    print("Real xi2 = ", xi2, "; theoretical = ", stats.chi2.ppf(0.95, df=L - 1))


def kolmogorovTestUniform(values):
    print(stats.kstest(values, stats.uniform(loc=0.0, scale=1.0).cdf))


