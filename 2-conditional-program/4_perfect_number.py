# Factors then Perfect and Primes
# 6 =1+2+3
# Factors of 6 is 1,2,3,6:

def perfect(n):
    
    res=0
    for i in range(1,n):
        if n%i==0:
            res=res+i
    
    if n==res:
        return True
    else:
        return False


x=perfect(int(input()))
if x:
    print("It is perfect")
else:
    print("It is not perfect")
