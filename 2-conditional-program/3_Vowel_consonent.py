a = input()
a=a.lower()
vov=0
con=0
for i in range(0,len(a)):
    if a[i] in ('a','e','i','o','u'):
        vov= vov+1
    elif a[i]>='a' and a[i]<='z':
        con=con+1

print("Number of vowel is ",vov)
print("Number of consonent is ",con) 

# ----------------------------------
# If vowel then in upper case and if consonent in lower
a = input()
a=a.lower() 
vov=0
con=0
a1=''
for i in range(0,len(a)):
    if a[i] in ('a','e','i','o','u'):
        c=a[i].upper()
        a1=a1+c
    elif a[i]>='a' and a[i]<='z':
        d=a[i].lower()
        a1=a1+d
    else:
        a1=a1+a[i]





