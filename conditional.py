# If/else
age = 16
if age >= 18:
    print("you are not adult")
else:
    print("you are an adult")


# if-elif-else Statement
    mark = 75
    if mark >= 80:
        print("A")
    elif mark >= 60:
        print("B")
    elif mark >= 40:
        print("C")
    else: 
        print("Fail")


# Logical Operators
income = 20
has_id = True
if income >= 22 and has_id:
    print("Allowed")
else: 
    print("Not Allowed") 
       
# Nested Condition
age = 20
if age >= 18:
    if age >= 21:
        print("You can drink")
    else:
        print("Adult but cannot drink")

# Short Form 
age = 18
status = "Adult" if age >= 25 else "Minor"
print(status)

# Real Example
num = int(-1)

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# testing
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


# more testing
money = int(input("please provide me the money:-"))

if money == 10:
    print("I will have a chocobar icecream")
else: 
    print("I will have a mango dolly")