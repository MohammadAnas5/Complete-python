n= int(input())

if n%2==0:
    print("It is even")
else:
    print("It is odd")    

print('------------------')
l2=[53,65,22,88,9]

for a in l2:
    if a%2==0:
        print(a)

print('------------------')
def even_odd(num):
    if num%2==0:
        return 'EVEN'
    else:
        return 'ODD'

print(even_odd(546))