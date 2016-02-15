#python 2.7 home task2
#'How are you? Eh, ok. Low or Lower? Ohhhh'
print 'Enter string'
s = raw_input()
a = []
for i in range(0, len(s)):
    if s[i].isupper() == True:
        a.append(s[i])
    else:
        continue
print(''. join(a))




#def incoding(s):
#a = []
#for i in range(0, len('s')):
#    if s[i].isupper() == True:
#        a.append(s[i])
#    else: continue
#return(''. join(a))

#print(incoding("How are you? Eh, ok. Low or Lower? Ohhhh"))