import random

memo = [0, 0, 0]

for i in range(10000000):
    t = random.randint(1, 3)
    memo[t-1] +=1

for i in range(3):
    p = float(memo[i])/10000000.0
    print(p, end=' ')