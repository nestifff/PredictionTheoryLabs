import matplotlib.pyplot as plt
import numpy as np

import lr1


def showLr1_1():
    startSeries = [13, 16, 20, 18, 21, 24, 25, 22, 28, 29, 25, 32, 33]
    simpleStep3 = lr1.simpleSmoothingOdd(series=startSeries, step=3)
    simpleStep5 = lr1.simpleSmoothingOdd(series=startSeries, step=5)
    simpleStep7 = lr1.simpleSmoothingOdd(series=startSeries, step=7)

    seriesDelete13 = startSeries
    seriesDelete13.pop()
    simpleStep4 = lr1.simpleSmoothingEven(seriesDelete13, step=4)

    polynomial5Degree = lr1.polynomial5DegreeSmoothing(startSeries)

    visualizePlot(startSeries)
    # visualizePlot(polynomial5Degree, color="black", skipFirst=2, skipLast=2)
    # visualizePlot(simpleStep4, color="black", skipFirst=2, skipLast=2)
    visualizePlot(simpleStep3, color="limegreen", skipFirst=1, skipLast=1)
    visualizePlot(simpleStep5, color="orange", skipFirst=2, skipLast=2)
    visualizePlot(simpleStep7, color="red", skipFirst=3, skipLast=3)
    showAllPlots()


def showLr1_2():
    m = -6
    sigma = 1.7

    normalSeries = np.random.normal(m, sigma, 240)
    parabolicTrend = lr1.getParabolicTrend()
    resultTrend = normalSeries + parabolicTrend

    resultTrendOddLength = list(resultTrend.copy())
    resultTrendOddLength.pop()
    resultTrendSmooth3 = lr1.simpleSmoothingOdd(resultTrendOddLength, 3)
    resultTrendSmooth9 = lr1.simpleSmoothingOdd(resultTrendOddLength, 9)
    resultTrendSmooth12 = lr1.simpleSmoothingEven(resultTrend, 12)

    visualizePlot(normalSeries, color="black", marker=".")
    visualizePlot(resultTrend, marker=".")
    visualizePlot(resultTrendSmooth3, color="limegreen", marker=".", skipFirst=1, skipLast=1)
    visualizePlot(resultTrendSmooth9, color="orange", marker=".", skipFirst=4, skipLast=4)
    visualizePlot(resultTrendSmooth12, color="red", marker=".", skipFirst=6, skipLast=6)
    showAllPlots()


def visualizePlot(values, color='slateblue', marker='o', skipFirst=0, skipLast=0):
    indices = list(range(skipFirst, len(values) - skipLast))
    newValues = []
    for (i, el) in enumerate(indices):
        indices[i] = el + 1
        newValues.append(values[el])
    plt.plot(indices, newValues, marker=marker, color=color)


def showAllPlots():
    plt.show()
