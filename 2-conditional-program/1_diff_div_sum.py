# Question -- differe

q= 498
# (4x9x8)-(4+9+8)   

sum=0
mul=1
while q!=0:
    rem=q%10
    sum=sum+rem
    mul=mul*rem
    q=q//10

print(mul-sum) 