"""
Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()

prompt user to enter number 
type cast to an int
store it as num 
new dictionary=()
for i in range of num
add i and i*i into disionary
print dictionary

"""
num=int(input("Enter a number: "))
storage={}
for i in range(1,num+1):
    storage[i]=i*i
    i=+1
print(storage)
