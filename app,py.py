a=int(input("Enter the number: "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,"Not a prime number")
            break
    else:
        print(a,"Prime Number")
if a<0:
    print("Not a prime number")