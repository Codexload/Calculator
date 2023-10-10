import sys
num = 1
while num <= 10000:
    def plus(a, b):
        plus1 = a + b
        return plus1
    def minus(a, b):
        minus1 = a - b
        return minus1
    def into(a, b):
        into1 = a * b
        return into1
    def devide(a, b):
        devide1 = a / b
        return devide1
#-------------------------------------------------------------------------------------------------
    number_one = int(input("Enter 1st Number--> "))
    condition = input("Enter Your Condition--> ")
    number_two = int(input("Enter 2nd Number--> "))
    if condition == "+":
        print(number_one, condition, number_two, "Is Equal To--> ", plus(number_one, number_two))
    elif condition == "-":
        print(number_one, condition, number_two, "Is Equal To--> ", minus(number_one, number_two))
    elif condition == "*":
            print(number_one, condition, number_two, "Is Equal To--> ", into(number_one, number_two))
    elif condition == "/":
        print(number_one, condition, number_two, "Is Equal To--> ", devide(number_one, number_two))
    else:
        print("Invalid Operator Entered.")
num += 1
sys.exit()