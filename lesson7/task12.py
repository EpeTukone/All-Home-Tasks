###### python 3.5 ######

def numbers(number):
    numbers_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}
    numerals = list(str(number))
    temp = [numbers_dict.get(int(i)) for i in numerals]
    return (' '.join(temp))

print('Enter the number')
print('results = {}'.format(numbers(input())))


