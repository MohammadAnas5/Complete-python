# 371 = 3x3x3 + 7x7x7 + 1x1x1


a=input("Enter the number : ")
length=len(a)
length=int(length)
n=int(a)
q=n
res=0
while q!=0:
    rem=q%10
    res=res+pow(rem,length)
    q=q//10

if res==n:
    print("It is armstrong")
else:
    print("It is not",res,n)
    



