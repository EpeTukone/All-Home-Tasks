import sys

n = int(sys.argv[1])
#print "enter n"
#n = input()
s = range(n)
sum = 0
print 'elements= {}'.format(s)
for i in range(len(s)-1):
    sum += s[i]
print 'sum of elements = {}'.format(sum)