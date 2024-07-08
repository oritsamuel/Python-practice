"""
Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.


create an empty array
create a range of numbers from 2000 and 3200
iterate between that range
if i%7 is 0 
and if i is not divisible by 5
add i to array.
 print array!
 """

storage=[]
for i in range(2000, 3200):
    if i%5!=0 and i%7==0:
           storage.append(i)
print(storage)
