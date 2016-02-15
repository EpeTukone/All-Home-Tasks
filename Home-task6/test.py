
import random
n = 3
l = random.sample(range(10 ** n), 10 ** n)
#l = [8, 7, 1, 5, 3, 4, 10, 2, 6, 9]
print l

#0i = 0
#temp_l = []
#for j in range(len(l) - 1):
#    for i in range(0,(len(l)-1), 2):
#        if l[i] > l[i + 1]:
#            l[i], l[i+1] = l[i+1], l[i]
#            temp_l.append(l[i])
#            temp_l.append(l[i+1])
#        elif l[i] < l[i+1]:
#            temp_l.append(l[i])
#            temp_l.append(l[i+1])
#        print i
#    i += 1
#    else: continue
#        print temp_l, i
#h = 1
#f = 1
for i in range(len(l) - 1):
#    print "hod", h,
    for j in range(len(l) - i - 1):
#        print "podhod", f
        if l[j] > l[j + 1]:
            l[j], l[j+1] = l[j+1], l[j]
#        print l
#        f += 1
#    h += 1
print l