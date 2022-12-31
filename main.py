# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import lr1Common

# lr1Common.showLr1_2()
# lr1Common.showLr1_1()

# distr = lr2.negBinomialDistribution(m=4, p=0.2, n=1000)
# lr2.pearsonNegBinomial(n=1000, m=4, p=0.2, distr=distr)
#
# distr2 = lr2.geometricDistribution(p=0.5, n=1000)
# lr2.pearsonGeometric(n=1000, p=0.5, distr=distr)

# iism.common.plotValuesList(distr2)
from iism.common import plotValuesList
from iism.lr1 import linearCongruentMethod, macLarenMarsagliaMethod, pearsonTestUniform, kolmogorovTestUniform
from iism.lr2 import negBinomialDistribution, geometricDistribution, pearsonNegBinomial, pearsonGeometric
from lr2.lr2 import showLr2_1, showLr2_2
from matplotlib import pyplot as plt
from statistics import mean, variance


N = 1000
sumGeom = 0
sumNegBinomial = 0

for k in range(N):
    print(k)
    errorsGeom = 0
    errorsNegBinomial = 0
    for i in range(10):
        geomDistr = geometricDistribution()
        negBinomialDistr = negBinomialDistribution()
        errorsNegBinomial += pearsonNegBinomial(negBinomialDistr)
        errorsGeom += pearsonGeometric(geomDistr)
    sumGeom += errorsGeom
    sumNegBinomial += errorsNegBinomial

print("errorsGeom = ", sumGeom / N)
print("errorsNegBinomial = ", sumNegBinomial / N)
