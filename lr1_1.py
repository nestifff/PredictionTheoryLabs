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


def getParabolicTrend(m=-6, sigma=1.7, size=240):
    series = []
    for t in range(0, size):
        series.append((0.5 * m * (t + 1) + sigma * (t + 1) ** 2) / 10000)
    return series
