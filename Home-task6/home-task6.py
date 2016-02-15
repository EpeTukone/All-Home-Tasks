###### benchscript py2.7 ######
import random
import datetime

h = 2
temp_time_py_sort = []
temp_time_u_sort = []
py_sort = []
u_sort = []
for n in range(2, 5): #7
    print "Degree N =", h
    l = random.sample(range(10 ** n), 10 ** n)
    temp_time_py_sort = []
    temp_time_u_sort = []

###### python sort test ######
    for p in range(5):
        print 'python sort step =', p + 1
        start = datetime.datetime.now()
        sort_l = sorted(l)
        finish = datetime.datetime.now()
        temp_time_py_sort.append(finish-start)

###### start processing results of python sort ######
    temp_time_py_sort.sort()
    temp_time_py_sort = temp_time_py_sort[1:4]
    avg_py_sort = (temp_time_py_sort[0] + temp_time_py_sort[1] + temp_time_py_sort[2]) / 3
    print temp_time_py_sort, "avg time sort", avg_py_sort
    py_sort.append(avg_py_sort)
###### end processing results of python sort ######


###### python sort test ######
    for u in range(5):
        print ' user sort step =', u + 1
        start = datetime.datetime.now()
        for i in range(len(l) - 1):
            for j in range(len(l) - i - 1):
               if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
        finish = datetime.datetime.now()
        temp_time_u_sort.append(finish-start)

###### start processing results of user sort ######
    temp_time_u_sort.sort()
    temp_time_u_sort = temp_time_u_sort[1:4]
    avg_u_sort = (temp_time_u_sort[0] + temp_time_u_sort[1] + temp_time_u_sort[2]) / 3
    print temp_time_u_sort, "avg time sort", avg_u_sort
    u_sort.append(avg_u_sort)
###### end processing results of user sort ######

    h +=1
print "results"
print py_sort
print u_sort


