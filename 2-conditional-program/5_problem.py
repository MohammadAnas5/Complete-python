# Kunal is allowed to go out with his friends only on the even days of a given month. Write a program to count the number of days he can go out in the month of August.

count=0
for i in range(0,30):
    if i%2==0:
        count+=1

print(count)
