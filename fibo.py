# Python program to print Fibonacci Series
def fibo(num):
    if num <= 1:
        return num
    else:
        return (fibo(num - 1) + fibo(num - 2))

num=int(input("Enter a number upto which the series will be generated : "))
if num <=0:
    print("Error, Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(num):
        print(fibo(i), end=" ")