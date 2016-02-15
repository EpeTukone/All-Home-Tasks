def sum_of_candies(kilo, cost):
    cost_of_candies = round(kilo * cost)

    return cost_of_candies

if __name__ == "__main__":
    print("All cost of candies = {}".format(sum_of_candies(4.6, 5)))


