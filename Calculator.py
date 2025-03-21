
cont = "n"
import numpy as np
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

def calculator():
    cont = ""
    while cont in ["y", "n", ""]:
        if cont == "y" or cont=="":
                num1 = float(input("Enter a number: "))
            operation = input("+ - *  \nEnter an operator: ")
            num2 = float(input("Enter another number: "))

            if operation == "+":
                print(add(num1,num2))
                num1 = add(num1,num2)
            elif operation == "-":
                print(sub(num1,num2))
                num1 = sub(num1,num2)
            elif operation == "*":
                print(mult(num1,num2))
                num1 = mult(num1,num2)
            elif operation == "/":
                print(div(num1,num2))
                num1 = div(num1,num2)
            else:
                print("Invalid operator")
                continue
            cont = input("Type y to continue with answer\nType n to start a new calculation")
        else:
            calculator()
calculator()


