import math

import numpy as np
from scipy import stats


def negBinomialDistribution(m=4, p=0.2, n=1000):
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


def geometricDistribution(p=0.25, n=1000):
    distr = []
    for i in range(n):
        a = np.random.uniform()
        distr.append(math.ceil(math.log(a) / math.log(1 - p)))
    return distr


def pearsonNegBinomial(distr, m=4, p=0.2, n=1000):
    values, counts = np.unique(distr, return_counts=True)
    xi2 = 0.0
    XI2Real = stats.chi2.ppf(0.95, df=m - 1)
    for i in range(m):
        tCount = math.comb(i + m - 1, i) * pow(p, m) * pow(1 - p, i) * n
        xi2 += (counts[i] - tCount) ** 2 / tCount
    # print("pearsonNegBinomial: ", xi2, "; theoretical: ", XI2Real)
    if xi2 > XI2Real:
        return 1
    else:
        return 0


def pearsonGeometric(distr, p=0.25, n=1000):
    maxValue = max(distr)
    counts = [0] * (maxValue + 1)
    for i in range(n):
        counts[distr[i]] += 1
    xi2 = 0.0
    XI2Real = stats.chi2.ppf(0.95, df=maxValue)
    for i in range(maxValue + 1):
        tCount = (1 - p) ** i * p * n
        xi2 += (counts[i] - tCount) ** 2 / tCount / n
    # print("pearsonGeometric: ", xi2, "; theoretical: ", XI2Real)
    if xi2 > XI2Real:
        return 1
    else:
        return 0

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
