#Simple Calculator
import time

n1 = input("Type your first number: ")
action = input("Select an action\nPlus, Minus, Divide, Multiply (or in symbol form): ")
n2 = input("Type your second number: ")

def calculate(n1, action, n2):
    if action == "Plus" or action == "+":
        return float(n1) + float(n2)
    elif action == "Minus" or action == "-":
        return float(n1) - float(n2)
    elif action == "Divide" or action == "/":
        return float(n1) / float(n2)
    elif action == "Multiply" or action == "*":
        return float(n1) * float(n2)
    else:
        return "Please specify an action as in example"

print("\n\nСalculation is carried out... ")
time.sleep(0.5)
print("\n*********************************")
print("Answer is: ")
print(calculate(n1, action, n2))
print("*********************************")
input("Press Enter to exit")
