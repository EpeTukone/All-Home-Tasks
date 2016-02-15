
def find_function(input_string, suffix):
    mas = input_string.split(' ')
    if suffix ==  str(mas[len(mas)-1]):
        print 'True'
    else:
        print 'False'
    return

if __name__ == '__main__':
    input_string = 'python is one of the best languges'
    suffix = 'languges'
    find_function(input_string, suffix)

