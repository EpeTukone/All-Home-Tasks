#hometask1 python 3.5
print('enter array range')
s = range(int(input()))
i = 1
res = 0
if len(s) <= 0:
    print("result: 0")
else:
    while i <= len(s)-1:
        res += s[i]
        i += 2
 #       if i > len(s)-1:
 #           break
    res = res * s[i-2]
    print("result: {}".format(res))