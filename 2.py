"""
Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

prompt user to input number
take that number and store in var x
fact=x
for i in range of x
multiply fact with x-1
x--

print fact
"""
fact=1
num=int(input("enter a number"))
for i in range(num):
    fact=fact*num
    num-=1
print(fact)
