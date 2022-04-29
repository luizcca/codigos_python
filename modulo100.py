n = 5
m = {}
for a in range(1,n+1):
    for b in range(1,n+a):
        m[a,b] = a*b


for f in range(1,100):
    if 100 % f == 0:
        print(f,sep='')

import string
longest = ""
for line in open(r"d:\python\IPS.txt", "r"):
    if len(line) > len(longest):
        longest = line
        print(longest.rstrip())


def soma(*args):
    total = 0
    for valor in args:
        total += valor
    return total


def produto(*args):
    total = 1
    for valor in args:
        total *= valor
    return total

def outer():
    v = 1
    def inner():
        nonlocal v
        v = 2
    inner()
    return v


