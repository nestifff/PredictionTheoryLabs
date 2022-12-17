# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import lr1
import lr1Common

startSeries = [13, 16, 20, 18, 21, 24, 25, 22, 28, 29, 25, 32, 33]
polynomial5Degree = lr1.polynomial5DegreeSmoothing(startSeries)
lr1.visualizePlot(startSeries)
lr1.visualizePlot(polynomial5Degree, color="green", skipFirst=2, skipLast=2)
lr1.showAllPlots()
# lr1Common.showSimple357(startSeries)

# seriesDelete13 = startSeries
# seriesDelete13.pop()
# simpleStep4 = lr1.simpleSmoothingEven(seriesDelete13, step=4)
#
# lr1.visualizePlot(startSeries)
# lr1.visualizePlot(simpleStep4, color="green")
# lr1.showAllPlots()

#  Провести сглаживание взвешенной скользящей средней –
# 5-точечное полиномом 2-й степени,



