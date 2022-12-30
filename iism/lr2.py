import math

import numpy as np
from scipy import stats


def negBinomialDistribution(m, p, n):
    distr = []
    q = 1.0 - p
    for i in range(n):
        tries = 0
        r = np.random.uniform()
        pCurr = pow(p, m)
        r -= pCurr
        while r > 0:
            tries += 1
            pCurr *= q * (m - 1 + tries) / tries
            r -= pCurr
        distr.append(tries)
    return distr


def geometricDistribution(p, n):
    distr = []
    for i in range(n):
        a = np.random.uniform()
        distr.append(math.ceil(math.log(a) / math.log(1 - p)))
    return distr


def pearsonNegBinomial(n, m, p, distr):
    values, counts = np.unique(distr, return_counts=True)
    xi2 = 0.0
    XI2Real = stats.chi2.ppf(0.95, df=m - 1)
    for i in range(m):
        tCount = math.comb(i + m - 1, i) * pow(p, m) * pow(1 - p, i) * n
        xi2 += (counts[i] - tCount) ** 2 / tCount
    print("pearsonNegBinomial: ", xi2, "theoretical ", XI2Real)


def pearsonGeometric(n, p, distr):
    maxValue = max(distr)
    counts = [0] * (maxValue + 1)
    for i in range(n):
        counts[distr[i]] += 1
    xi2 = 0.0
    XI2Real = stats.chi2.ppf(0.95, df=maxValue - 1)
    for i in range(maxValue + 1):
        tCount = (1 - p) ** i * p * n
        xi2 += (counts[i] - tCount) ** 2 / tCount
    print("pearsonGeometric: ", xi2, "theoretical ", XI2Real)

# void pearsonTestForGeometric(double p, vector<int> geodist) {
#    sort(geodist.begin(), geodist.end());
#    int max = geodist[N - 1];
#    vector<int> nCount(max + 1, 0);
#    double xi_2 = 0.0, XI_2 = calculateXi2ForPearsonTest(max);
#    for (int i = 0; i < N; i++)
#       ++nCount[geodist[i]];
#    for (int i = 0; i <= max; i++)
#    {
#       double tCount = pow(1 - p, i) * p * N;
#       xi_2 += pow(nCount[i] - tCount, 2) / tCount;
#    }
#    if (xi_2 < XI_2)
#       cout << endl << "Pearson test: " << xi_2 << " < " << XI_2 << " => true sequence" << endl;
#    else
#       cout << endl << "Pearson test: " << xi_2 << " > " << XI_2 << " => false sequence" << endl;
# }
