a=None
                       
sum=0
mul=1
max=0
while a!=0:
    a1=input()
    a=int(a1)
    sum = sum+a
    mul= mul+a
    
    if max<a:
        max=a

print("Sum is:",sum,"\nMaximum : ",max) 