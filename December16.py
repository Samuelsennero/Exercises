import random

def randomlist(a):
    new = []
    for i in range(a):
        new.append(random.randint(0, 100))
    return new

print(randomlist(7))

def win(a):

    if a == randomlist[0]:
        return ("Du vann")
    
    elif a == randomlist[1]:
        return ("Du vann")
    
    elif a == randomlist[2]:
        return ("Du vann")
    
    elif a == randomlist[3]:
        return ("Du vann")
    
    elif a == randomlist[4]:
        return ("Du vann")
    
    elif a == randomlist[5]:
        return ("Du vann")
    
    elif a == randomlist[6]:
        return ("Du vann")
    else:
        return ("Du vann inte")

print(win(random.randint(0, 100)))
