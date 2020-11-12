#Excersie: Faulty Calculator
# 45*3,  =555, 56+9 = 77, 56/6 = 4
#Design a calculator which will correctly solve all the problems except the following ones:
#your program shouyld take operator and the two number input from users
# And return result
print("Welcome to calculation")
print(["+,-,*,**,/,%"])
print("Enter 1st Number:")
num1 = int(input())
print("Enter 2nd Number")
num2 = int(input())
print("Enter your mathematical Operator" + "+,-,*,**,/,%")
num3 = input()

if num1 == 45 and num2 == 3 and num3 == "*":
    print(int(555))
elif num1 == 56 and num2 == 9 and num3 == "+":
    print(int(77))
elif num1 == 56 and num2 == 6 and num3 == "/":
    print(int(4))
elif num3 == "+":
    add=num1+num2
    print(add)
elif num3 == "-":
    substract=num1 - num2
    print(substract)
elif num3 == "*":
    multiply=num1*num2
    print(multiply)
elif num3 == "/":
    devide=num1/num2
    print(devide)
elif num3 == "**":
    square=num1**num2
    print(square)
elif num3 == "%":
    mod=num1%num2
    print(mod)
else:
    print("Error! Please check your input")