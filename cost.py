import numpy

def updateCost(cost, originalCost, sigma, sales):
    # cost = numpy.random.normal(cost, cost*sigma)
    cost += cost * numpy.random.normal(0, sigma)
    cost += sales*0.05
    return cost
