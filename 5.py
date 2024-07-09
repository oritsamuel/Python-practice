"""
Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

Hints: Use init method to construct some parametersz

create method getString
has input function to get string from user 
create method printString 
it takes input from getString function
changes it to capital
prints it out
"""
class myClass:
    def getString(self):
        global myStr
        myStr = input("enter a sentece")
    def printString(self):
        print(myStr.upper())

test=myClass()
test.getString()
test.printString()   

