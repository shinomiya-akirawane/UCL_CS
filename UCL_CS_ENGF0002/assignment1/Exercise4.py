import random

def estimate_pi(precision):
    tot=0
    numOfGeneratedNumbers=1000000000
    for n in range(1,numOfGeneratedNumbers):
        x=random.random()
        y=random.random()
        if(x*x+y*y<=1):
            tot+=1
    pi=(4*tot)/numOfGeneratedNumbers
    return round(pi,precision)

precision=int(input("Please input the precision: "))
print(estimate_pi(precision))
