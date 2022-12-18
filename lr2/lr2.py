import numpy as np

from lr1 import lr1Common


def exponentialSmoothing(series, startValuesNum, param):
    firstValue = sum(series[:startValuesNum]) / startValuesNum
    smoothing = []
    smoothing.append(firstValue)
    for t in range(0, len(series) - 1):
        nextValue = (1 - param) * smoothing[len(smoothing) - 1] + param * series[t]
        smoothing.append(nextValue)
    return smoothing


def getMAPE(predictValue, realValue):
    return abs((realValue - predictValue) / realValue) * 100


def showLr2_1():
    startSeries = [13, 16, 20, 18, 21, 24, 25, 22, 28, 29, 25, 32, 33]
    startValuesNums = [6, 12]
    params = [0.1, 0.3, 0.5, 0.7, 0.9]
    for i in range(0, len(startValuesNums)):
        for j in range(0, len(params)):
            print("startValuesNum = ", startValuesNums[i], "param = ", params[j])
            resultTrendSmooth = exponentialSmoothing(startSeries, startValuesNum=startValuesNums[i], param=params[j])
            print("MAPE = ", getMAPE(resultTrendSmooth[len(resultTrendSmooth) - 1], startSeries[len(startSeries) - 1]))

    # лучшее с startValuesNum = 12, param = 0.9
    lr1Common.visualizePlot(startSeries)
    # lr1Common.visualizePlot(lr2.exponentialSmoothing(startSeries, startValuesNum=12, param=0.5), color="green")
    lr1Common.visualizePlot(exponentialSmoothing(startSeries, startValuesNum=12, param=0.9), color="orange")
    lr1Common.showAllPlots()


def showLr2_2():
    startValuesNum = 239
    param = 0.9
    normalSeries = np.random.normal(-6, 1.7, 240)
    resultExponentSmoothing = exponentialSmoothing(normalSeries, startValuesNum, param)
    lr1Common.visualizePlot(normalSeries, marker=".")
    lr1Common.visualizePlot(resultExponentSmoothing, color="orange", marker=".")
    lr1Common.showAllPlots()
    realValue = normalSeries[len(normalSeries) - 1]
    predictValue = resultExponentSmoothing[len(resultExponentSmoothing) - 1]
    print("realValue = ", realValue, "; predictValue = ", predictValue)
    print("MAPE = ", getMAPE(realValue=realValue, predictValue=predictValue))
