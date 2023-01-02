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
from iism.lr3 import normalDistribution, laplasDistribution, exponentialDistribution
from lr2.lr2 import showLr2_1, showLr2_2
from matplotlib import pyplot as plt
from statistics import mean, variance

distr = normalDistribution()
laplasDistr = laplasDistribution()
expDistr = exponentialDistribution()
print("Распределение Лапласа")
print("Истинное мат ожидание: ", mean(laplasDistr), ', непрерывная оценка:', 0)
print("Истинная диссперсия", variance(laplasDistr), ', непрерывная оценка:', 2 / 1 ** 2)
print("Экспоненциальное Распределение")
print("Истинное мат ожидание: ", mean(expDistr), ', непрерывная оценка:', 1 / 4)
print("Истинная диссперсия", variance(expDistr), ', непрерывная оценка:', 1 / 4 ** 2)
