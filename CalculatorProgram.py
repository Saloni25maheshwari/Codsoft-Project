def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num2 ==0:
        return "Cannot divide by zero"
    return num1/num2




print("Select Operations")
print(
"1. Addition\n"
"2. Subtraction\n"
"3. Multiplication\n"
"4. Division\n"
"5. Quit")

Choice = int(input("Enter the operation to be perform: 1,2,3,4 or 5"))

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if Choice==1:
    print("The Addition is",num1,"+",num2,"=" , add(num1,num2))
elif Choice==2:
    print("The Subtraction is",num1,"-",num2,"=" , subtract(num1,num2))
elif Choice==3:
    print("The Multiplicationis",num1,"*",num2,"=" , multiply(num1,num2))
elif Choice==4:
    print("The Division is",num1,"/",num2,"=" , divide(num1,num2))
else:
    print("Invalid Input")





