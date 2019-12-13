
def divisble_by(a, b):
    return a % b == 0
    
for i in range(1000):
    if divisble_by(i, 7) == True and divisble_by(i,2) == False:
        print(i)

#GithubTest