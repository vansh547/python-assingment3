n=int(input("enter a number: "))

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)
    
print(f"factorial of {n} is {factorial(n)}")