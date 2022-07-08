# For string
a='1234'
print(len(a))


#1 For number

b=345

count=0
while b!=0:
    b=b//10
    count = count+1

print("Length of number is :",count)

#2

b=int(len(a)) 
print(type(b))
