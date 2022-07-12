# Write a program to print the sum of negative numbers, sum of positive even numbers and the sum of positive odd numbers from a list of numbers (N) entered by the user. The list terminates when the user enters a zero.

a=None
b=[]
while a!=0:
    a=input()
    a=int(a)
    b.append(a)

sum_e=0
sum_o=0
sum_n=0
for i in b:
    if i<0:
        sum_n+=i
    elif i>=0:
        if i%2==0:
            sum_e+=i
        else:
            sum_o+=i

    
print("Sum of negative numbers ",sum_n)
print("Sum of +ive odd numbers ",sum_o)
print("Sum of +ive even numbers ",sum_e) 
print("List is ",b)




