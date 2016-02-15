def function_if(number1, number2):
    if number1 == number2:
        r = '0'
    elif number1 > number2:
        r = '1'
    elif number1 < number2:
        r = '-1'
    return r

if __name__ == '__main__':
    a = 4
    b = 5
    print 'result: {}'.format(function_if(a, b))