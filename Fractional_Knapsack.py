class ItemValue:
    def __init__(self, wt, val, item):
        self.wt = wt
        self.val = val
        self.item = item
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


def solveKnapsack(weights, profits, items, capacity):

    items_list = []
    for i in range(len(weights)):
        items_list.append(ItemValue(weights[i], profits[i], items[i]))

    # sorting items by value
    items_list.sort(reverse=True)

    knapsack_value = 0
    knapsack = []
    knapsack_weights = []

    for item in items_list:
        if capacity - item.wt >= 0:
            capacity -= item.wt
            knapsack_value += item.val
            knapsack.append(item.item)
            knapsack_weights.append(item.wt)

        else:
            fraction = capacity / item.wt
            knapsack_value += item.val * fraction
            knapsack.append(item.item)
            knapsack_weights.append(fraction)
            capacity -= int(item.wt * fraction)
            break

    return knapsack, knapsack_weights, knapsack_value


if __name__ == "__main__":
    items_list = ["A", "B", "C", "D", "E", "F", "G"]
    profits = [10, 5, 20, 7, 6, 18, 3]
    weights = [2, 3, 5, 7, 1, 5, 1]
    capacity = 16

    knapsack, knapsack_weights, knapsack_value = solveKnapsack(weights, profits, items_list, capacity)
    print("Items in Knapsack =", knapsack)
    print("Weights =", knapsack_weights)
    print("Maximum profit in Knapsack =", knapsack_value)
