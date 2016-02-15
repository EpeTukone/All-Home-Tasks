######  python 3.5 ######

a = tuple('123456789')

def tuple_function(tuple_):
    b = list(a)
    new_tuple = tuple([i for i in b if int(i) % 2 == 0])
    return new_tuple

print("new tuple: {}".format(tuple_function(a)))