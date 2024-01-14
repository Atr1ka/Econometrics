import matplotlib.pyplot as plt, mpld3

class Graph:
    def __init__(self, name, cost):
        self.cost = cost
        self.initialCost = cost
        self.t = [0] 
        self.v = [cost]
        plt.title(name)
        plt.xlabel("Day")
        plt.ylabel("Cost")

    def update(self, time, cost, refresh):
        self.t.append(time)
        self.v.append(cost)
        plt.plot(self.t, self.v)
        if (refresh):
            mpld3.show()
    def show(self):
        mpld3.show()