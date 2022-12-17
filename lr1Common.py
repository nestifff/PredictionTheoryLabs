import lr1


def showSimple357(startSeries):
    simpleStep3 = lr1.simpleSmoothingOdd(series=startSeries, step=3)
    simpleStep5 = lr1.simpleSmoothingOdd(series=startSeries, step=5)
    simpleStep7 = lr1.simpleSmoothingOdd(series=startSeries, step=7)

    lr1.visualizePlot(startSeries)
    lr1.visualizePlot(simpleStep3, color="green", skipFirst=1, skipLast=1)
    lr1.visualizePlot(simpleStep5, color="orange", skipFirst=2, skipLast=2)
    lr1.visualizePlot(simpleStep7, color="red", skipFirst=3, skipLast=3)
    lr1.showAllPlots()
