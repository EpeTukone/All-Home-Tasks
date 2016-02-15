import random
string = []
s = random.sample(range(130), 130)
print s
for i in s:
    if i == 42:
        print "The answer......"
        break
    else:
        if i < 99:
            string.append(i)
print "result = {}".format(string)