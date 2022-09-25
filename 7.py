# 1. Write a python script to display the number of days in a given month number.
# code: 
# n=int(input("Enter the month number: "))
# match n:
#     case n if n in (1,3,5,7,8,10,12):
#         print("31 number of days")
#     case n if n in (4,6,9,11):
#         print("30 number of days")
#     case n if n == 2 :
#         print("28 or 29 number of days")
#     case _:
#         print("Invalid month number")
    
# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
# code: 
# print("Enter 1: for Addition")
# print("Enter 2: for Subtraction")
# print("Enter 3: for Multiplication")
# print("Enter 4: for Division")
# n=int(input())
# num1=int(input("Enter first numbers: "))
# num2=int(input("Enter second number: "))
# match n:
#     case 1: 
#         print(num1+num2)
#     case 2:
#         print(num1-num2)
#     case 3:
#         print(num1*num2)
#     case 4:
#         print(num1/num2)
#     case _:
#         print("Invalid number")

# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

# code:
# print("What to you want to check")
# print("a. Check whether a given set of three numbers are lengths of an isoscelestriangle or not")
# print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
# print("c. Check whether a given set of three numbers are equilateral triangle or not")
# print("d. Exit")
# var = input("")
# match var:
#     case 'a' :
#         print("Enter three sides of triangle: ")
#         x,y,z = int(input()),int(input()),int(input())
#         if x==y or x==z or y==z:
#             print("Triangle is isoscles")
#         else:
#             print("Triangle is not an isoscles")
#     case 'b':
#         print("Enter the hypotunose,base and perpendicular")
#         h,b,p = int(input()),int(input()),int(input())
#         if h**2 == P**2 + b**2:
#             print("Triangle is right angled")
#         else:
#             print("Triangle is not right angled")
#     case 'c':
#         print("Enter the length of sides of triangle: ")
#         x,y,z = int(input()),int(input()),int(input())
#         if x==y and x==z and y==z:
#             print("Triangle is equilateral")
#         else:
#             print("Triangle is not an equilateral")
#     case _:
#         exit

# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.
# code: 

# n=int(input("Enter your age: "))
# match n:
#     case n if n<10:
#         print("Kid")
#     case n if n<20:
#         print("Teen")
#     case n if n<40:
#         print("young")
#     case n if n<60:
#         print("experienced")
#     case n if n>60:
#         print("Senior Citizen")
#     case _: 
#         print("You are not in any category")

# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.
# code: 
# n=int(input("Enter a number: "))
# match n:
#     case n if n%2==0:
#         print("Saurabh Shukla")
#     case n if n%2!=0 and n<0:
#         print("Prateek Jain")
#     case n if n%2!=0 and n>0:
#         print("Aditya Choudhary")

# 6. Write a python program to check whether a given string is a multiword string or single
# word string using match case statement
# code: 
# n = input("Enter a string: ")
# n = n.strip() # remove first and last extra space or string
# match n:
#     case n if ' ' in n:
#         print("Multiword word string")
#     case n if ' ' not in n:
#         print("singleword string")

# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement
# code: 
# n=int(input("Enter a number: "))
# match n:
#     case n if n<0:
#         print("Negative")
#     case n if n>0:
#         print("Positive")
#     case n if n==0:
#         print("Zero")

# 8. Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement
# code: 
# s1=input("Enter first string : ")
# s2=input("Enter second string: ")
# match (s1,s2):
#     case (s1,s2) if s1==s2:
#         print("Strings are identical")
#     case (s1,s2) if s1>s2:
#         print("First string comes after second string")
#     case (s1,s2) if s1<s2:
#         print("First string comes before second string")

# 9. Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year
# code: 
# n=int(input("Enter the year: "))
# match n:
#     case n if n%100!=0 and n%4==0:
#         print("Non century leap year")
#     case n if n%400==0:
#         print("Century leap year")
#     case n if n%100!=0 and n%4!=0:
#         print("Non century non leap year")
#     case n if n%400!=0:
#         print("Century non leap year")

# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday
# code: 
# sen=(input("Enter the colour name in sentence: "))
# match sen :
#     case sen if "yellow" in sen:
#         print("Monday")
#     case sen if "blue" in sen:
#         print("Tuesday")
#     case sen if "orange" in sen:
#         print("Wednesday")
#     case sen if "white" in sen:
#         print("Thursday")
#     case sen if "black" in sen:
#         print("Friday")
#     case sen if "red" in sen:
#         print("Saturday")
#     case _:
#         print("Sunday") 