from math import floor
# /  division
print("'/' : division",5/3)
print("// : floor division",5//3)
print(floor(5/3))

# Original number is equal to reverse number
# abc % 10 = c
# arrange the remainder for new number, we get a revere number
# abc // 10 = a

number=0
num= int(input("Enter the string "))
n=num

while n!=0:
    rem= n%10
    number= (number*10)+rem
    n=n//10

if(num==number):
    print("It is palendrome")
else:
    print("It is Not palendrome")









print('-----------------------')


def isPalendrome1(n1):
    rev = ''.join(reversed(n1))

    if n1==rev:
        return True
    else:
        return False   

print('-----------------------')

def isPalendrome2(n1):
    rev = n1[::-1]

    if n1==rev:
        return True
    else:
        return False 




z=isPalendrome2("343")
if z :
    print("It is palendrome")
else:
    print("It is not palendrome")    