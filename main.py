import cost
from graph import Graph

if __name__ == "__main__":
    price = 1000
    # print(price)
    stock1 = Graph("Stock 1", 1000)
    for time in range(1, 10000):
        price = cost.updateCost(price, 1000, 0.05, 0)
        stock1.update(time, price, False)
        # print(price)
    stock1.show()