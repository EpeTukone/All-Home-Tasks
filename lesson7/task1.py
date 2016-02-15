######task1######

a = 2
b = 3
c = 5
if a > b and a > c and b > c:
    sum = a + b
elif a > b and a > c and c > b:
    sum = a + c
elif b > a and b > c and c > a:
    sum = b + c
elif b > a and b > c and a > c:
    sum = b + a
elif c > a and c > b and b > a:
    sum = c + b
elif c > a and c > b and a > b:
    sum = a + b
print sum

