from matplotlib import pyplot as plt


def plotValuesList(values, color="blue"):
    for i, value in enumerate(values):
        plt.plot(i, value, marker=".", color=color)
    plt.xlabel("n")
    plt.ylabel("error")
    plt.show()
