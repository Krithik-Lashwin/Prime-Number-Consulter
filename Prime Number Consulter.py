a = int(input('Enter the number: '))
isprime = True
if(a == 1):
    print('This is neither a prime or composite number')
elif(a == 2):
    print('This is a prime number')
else:
    for i in range(2,a):
        if(a%i == 0):
            isprime = False
            break
    if(isprime == True):
        print('This is a prime number')
    else:
        print('This is a composite number')