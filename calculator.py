
#Add
def add(n1,n2):
    return n1+n2
#Subtract
def subtract(n1,n2):
    return n1-n2
#Multiply
def multiply(n1,n2):
    return n1*n2
#Divide
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
num1= int(input("What is the first number  :"))
for symbol in operations:
    sym=symbol
    print(sym)
oparetion_symbol=input("Pick an operation from the line above: ")
num2= int(input("What is the second number :"))
calculetion_function =operations[oparetion_symbol](num1,num2)
print(f"{num1} {oparetion_symbol} {num2}= {calculetion_function}")