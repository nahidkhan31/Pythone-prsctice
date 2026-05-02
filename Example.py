num1 = float(input("First Num: "))
num2 = float(input("Second num: "))

if num1 > num2:
    print(f"Big Number is: {num1}")
elif num2 > num1:
    print(f"Big Number is: {num2}")
else:
    print("both are equal")

# 

gender = input("Choose One (M/F): ").upper()

if gender == 'M':
    print("Good Morning Sir")
elif gender == 'F':
    print("Good Morning Ma'am")
else:
    print("Good Morning!")

# 

name = input("Write your name: ")
age = int(input("Write your age: "))

if age >= 18:
    print(f"Hello {name}, you are a valid voter.")
else:
    print(f"Sorry {name}, you are not a valid voter yet.")