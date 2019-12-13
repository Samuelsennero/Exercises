import random

def randomlist(a):
    new = []
    for i in range(a):
        new.append(random.randint(0, 100))
    return new

print(randomlist(11))