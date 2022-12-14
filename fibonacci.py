""" Program to print fibonacci series of a given number """

def fibonacci(n):
    a=0
    b=1
    if n <= 0:
        print("Please enter positive number")
    elif n == 0:
        print(a)
    else:
        print("The fibonacci series of {} is: ".format(n))
        print(a, end = " ")
        print(b, end = " ")
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
            print(c, end = " ")

n = int(input("Enter the value: "))
fibonacci(n)



