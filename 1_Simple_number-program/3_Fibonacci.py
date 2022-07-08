# Not using loop's "i" directly
num = int(input("Enter the number "))

a=0
b=1

for i in range(1,num+1):
    print(a) # for series
    c=a+b
    a=b
    b=c 

print("Directly Fibonacci number :",b-a)  # for fibo number