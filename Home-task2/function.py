def incoding(s):
    a = []
    for i in range(0, len(s)):
        if s[i].isupper() == True:
            a.append(s[i])
    return(''.join(a))
​
f = incoding('How are you? Eh, ok. Low or Lower? Ohhhh')