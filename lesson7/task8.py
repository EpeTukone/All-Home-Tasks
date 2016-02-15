def function(*args):
    print args
    return sum(args)

if __name__ == "__main__":
    print("sum = {}".format(function(465, 1223, 54, 98, 433, 678)))