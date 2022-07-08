a = input(" Enter the number ")
length=int(len(a))
count=0
q=int(a)
res=0
while q!=0:
    rem=q%10
    res=res+(rem*pow(2,count))
    count = count+1
    q=q//10

print("Decimal number is ",res)

