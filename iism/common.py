from matplotlib import pyplot as plt


def plotValuesList(values, color="red"):
    for i, value in enumerate(values):
        plt.plot(i, value, marker=".", color=color)
    plt.xlabel("step")
    plt.ylabel("value")
    plt.show()
