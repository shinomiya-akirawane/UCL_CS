def Fizzbuzz():
    num=[]
    for n in range(0,101,1):
        num.append(n)
    for n in range(0,101,3):
        num[n]="Fizz"
    for n in range(0,101,5):
        if(num[n] != "Fizz"):
            num[n]="Buzz"
        else:
            num[n]="FizzBuzz"
    print(num[1:101])

Fizzbuzz()
