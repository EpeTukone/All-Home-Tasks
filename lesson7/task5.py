import random
s = random.sample(range(100), 100)
for i in s:
    if i % 13 > 0 or i == 0:
        continue
    else:
        print i