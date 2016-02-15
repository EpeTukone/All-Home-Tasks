#

def print_format_string(s):
    for i in s:
        if i % 2 ==0:
            print "An even number: 2 = {}".format(i)
        else:
            print "An even number: 3 = {}".format(i)


if __name__ == "__main__":
    s = [1, 5, 7, 9, 10, 12]
    print print_format_string(s)