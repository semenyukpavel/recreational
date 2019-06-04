import random
import math


def prob (n):
    return 1/(n+1)

def jump (n):
    s = random.random()
#    print(s, prob(n))
    if 0<s< prob(n):
        return 1
    else:
        return n+1

def harm (n):
    s = 0
    for i in range(n):
        s+=1/(i+1)
    return(s)

a = list()

mean = 0
for t in range(10000):
    sum = 0
    for j in range(100):
        n = 1
        k = 1
        flag = False
        while(flag==False):
            k = n
            n = jump(n)
            if n == 1:
                flag = True
#        print(j, 'step; value = ', k)
        a.append(k)
        sum+=k
#    print(sum/(j+1), 'max = ', max(a))
    mean+=sum/(j+1)
print('expected maximum =', harm(100))
mean/=10000
print('mean = ', mean)

