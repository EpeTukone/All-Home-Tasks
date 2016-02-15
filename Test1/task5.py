d = {1: '12', 2: '4', 3: '3', 4: '15', 5: '8', 6: '6'}
#d = {1: '12', 2: '4', 3: '7', 4: '15', 5: '8'}

s = str([i for i in d if i == int(d.get(i))])
if len(s) == 0:
    print 'no values = keys'
else:
    print "key('s):{} = value('s):{}".format(s, s)




# for i in len(d):
#     if i == int(d.get(i)):
#         print 'key:{} = value:{}'.format(i, d.get(i))
#     elif i > len(d) and i != int(d.get(i)):
#         continue
#     elif i == len(d) and i == int(d.get(i)):
#         print 'no values = keys'
#         break
