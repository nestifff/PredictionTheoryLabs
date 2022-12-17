import matplotlib.pyplot as plt


def visualizePlot(values, color='blue', skipFirst=0, skipLast=0):
    indices = list(range(skipFirst, len(values) - skipLast))
    newValues = []
    for (i, el) in enumerate(indices):
        indices[i] = el + 1
        newValues.append(values[el])
    plt.plot(indices, newValues, marker='o', color=color)


def showAllPlots():
    plt.show()


def simpleSmoothingOdd(series, step):  # нечетное
    smoothing = []
    halfStep = int((step - 1) / 2)
    for t in range(0, halfStep):
        smoothing.append(series[t])
    for t in range(halfStep, len(series) - halfStep):
        sumCurr = 0
        for i in range(-halfStep, halfStep + 1):
            sumCurr += series[t + i]
        smoothing.append(sumCurr / step)
    for t in range(len(series) - halfStep, len(series)):
        smoothing.append(series[t])
    return smoothing


def simpleSmoothingEven(series, step):  # четное
    smoothing = []
    halfStep = int(step / 2)
    for t in range(0, halfStep):
        smoothing.append(series[t])
    for t in range(halfStep, len(series) - halfStep):
        sumCurr = 0
        for i in range(-halfStep, halfStep + 1):
            if i == -halfStep or i == halfStep:
                sumCurr += 0.5 * series[t + i]
            else:
                sumCurr += series[t + i]
        smoothing.append(sumCurr / step)
    for t in range(len(series) - halfStep, len(series)):
        smoothing.append(series[t])
    return smoothing


def polynomial5DegreeSmoothing(series):
    smoothing = []
    halfStep = 2
    for t in range(0, halfStep):
        smoothing.append(series[t])
    for t in range(halfStep, len(series) - halfStep):
        sumCurr = 0
        for i in range(-halfStep, halfStep + 1):
            if i == -2 or i == 2:
                sumCurr += -3 * series[t + i]
            elif i == -1 or i == 1:
                sumCurr += 12 * series[t + i]
            else:
                sumCurr += 17 * series[t + i]
        smoothing.append(sumCurr / 35)
    for t in range(len(series) - halfStep, len(series)):
        smoothing.append(series[t])
    return smoothing
