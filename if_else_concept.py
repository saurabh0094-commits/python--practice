""" a = 20
b= 20

if a>b:
    print(f"a={a} is greater then b={b}")
elif a==b:
    print("Both are equal")
else:
    print(f"b={b} is greater") """

""" x=int(input("enter value of x"))
y=int(input("enter value of y")) 
if x>y:
    print(f"x={x} is greater than y={y}")  
elif x==y:
    print(f"Both are equal")   
else:
    print(f"y={y} is greater") """   
#1. Write a program to check if a number is positive or negative.
""" a=int(input("enter value of a"))
if a>=0:
    print(f"number is positive")
else:
    print(f"number is negative") """
#2. Write a Python program to check whether a number is even or odd using if-else
""" a=int(input("enter no:"))  
if a%2==0:
    print(f"no is even")     
else:
    print("odd") """
#3. Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and 60, and 'Senior' if 60 or above
""" age=int(input("Enter age:"))
if age<18:
    print("Minor")
elif age<=60:
    print("Adult")
else:
    print("Senior") """

#5. Write a Python program to check if a number is divisible by 3 and 5 both.
""" Number=int(input("Enter a Number"))
if Number%3==0 and Number%5==0:
    print("Number is divisible by both 3 and 5")
else:
    print("Numberis not divisible by both 3 and 5") """
#6. Write a Python program to input marks of a student and print the grade: - 90-100 → A - 80-89 → B - 70-79 → C - 60-69 → D - <60 → F
""" marks=int(input("Enter marks"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
else:
    print("Fail") """
#7. Write a program that takes input for two numbers and prints which one is greater or if they are equal
""" x=int(input("Enter number"))
y=int(input("Enter number"))
if x>y:
    print(f"x={x}) is greater than y={y}")
elif x==y:
    print(f"Both are equal")
else:
    print(f"y={y} isgreater") """
#8. Write a program that checks whether a year is a leap year or not.
""" year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("It is a leap year")
else:
    print("It is not a leap year") """
#9. Write a Python program that simulates a simple login system with a stored username and password. Use if-else to check credentials.
""" username=input("enter username")
password=input("enter passwrod")
if username=="saurabh" and password=="123@":
    print("login Successful")
else:
    print("Wrong Credentials") """
#16. Electricity Bill Calculator (slab wise)
""" units = int(input("Enter units consumed:")) """

#First 100 units = 100 × 5 = ₹500
#Next 100 units = 100 × 7 = ₹700
#Remaining 50 = 50 × 10 = ₹500
#Total bill = ₹1700
""" if units <= 100:
    bill = units * 5
    print("Electricity Bill:", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Electricity Bill:", bill)
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Electricity Bill:", bill) """
#18. Grading System based on average marks
""" marks1=int(input("Enter marks for Subject1:"))
marks2=int(input("Enter marks for Subject2:"))
marks3=int(input("Enter marks for Subject3:"))
average=(marks1+marks2+marks3)/3

if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else: 
    print("F") """
# SI with different rates for each year
""" principal = float(input("Enter principal amount: "))
years = int(input("Enter number of years: "))

if years == 1:
    rate = 5
elif years == 2:
    rate = 6
else:
    rate=7
SI = principal * rate * years / 100
print("SI", SI) """
#10. Write a calculator program that takes two numbers and an operator (+, -, *, /) from the user and performs the operation using if-elif-else.
""" num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operator") """
#4. Write a program that checks if a character entered is a vowel or a consonant.
character = input("Enter a Character: ")
if character in "aeiou":
    print("Vowel")
else:
    print("Consonent") 