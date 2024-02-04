is_male=False
if is_male:
    print("your are male")
else:
    print("you are a female") 
def max(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print( max(6,3,9) )  
num1=float(input("Enter first number")) 
op=(input(str("Enter operator")))
num2=float(input("Enter third number"))
if op == str("+"):
    print("fgdhd")
    print(num1 + num2)
elif op == str("-"):
    print(num1 - num2)
elif op == str("*"):
    print(num1 * num2)
elif op == str("/"):
    print(num1 / num2)

