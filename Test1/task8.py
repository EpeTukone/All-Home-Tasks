file_ = open('text.txt', 'r').readlines()
counter = 0
for i in range(len(file_)):
    if len(file_[i]) == 1:
        counter += 1
    else:
        continue
print "zero string:{}".format(counter)
