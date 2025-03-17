# Write a Python program that takes a character as input and checks whether
# it is a vowel or not. Use the
# if-else statement



# alphabet = input("enter an alphabet :")
# vowels = ("a","e","i","o","u")
# if alphabet == vowels:
#     print("welcome back, you entered an vowel :")
# else:
#     print("welcome back, you enterd not an vowel")

# Write a program that takes an age as input and classifies the person into
# one of the following age groups:

# Child: 012 years
# Teenager: 1317 years
# Adult: 1864 years
# Senior: 65 years and older
# age = int(input("enter your age :"))
# if age <= 12 :
#     print("hello,you entered below 12 years ,your a child ")
# elif age <= 17:
#     print("hello,you entered below 17 years ,your a teenager")
# elif age <= 64:
#     print("hello,you entered below 64 years ,your an adult")
# else:
#     print("hello,you entered above 65 years ,your an senior")
    
# Write a program that takes an integer as input and classifies it as positive,
# negative, or zero. Use the
# if-elif-else statement.

# number = int(input("enter a number :"))
# if number <= 0:
#     print("hello, you enterd below zero,its a negative number ")
# elif number == 0 :
#     print("you entered a zero :")
# else:
#     print("you entered a positive number")


# Create a program that checks whether a given year is a leap year or not. A
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.

# year = int(input("enter the year :"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
#     print(f"you year is a leap year {year}")
# else :
#     print(f"your year is  not a leap year {year}")

# # Build a simple calculator program that takes two numbers and an operator
# (+, -, *, /) as input and performs the corresponding operation.
# num_1 = 20
# num_2 = 12
# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)
# print(num_1 / num_2)

# Rewrite the following code using the short-hand
# if statement:
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd"
# number = 8
# result = "its a even number" if number % 2 == 0 else "its a odd number"

# x = 8
# result = "Even" if x % 2 == 0 else "Odd"


# Create a program that calculates the final price after applying a discount.
# The program should take the original price and the discount percentage as
# input.

# product_price = 10000
# discount_given = int(input("enter a discount in (%) :"))
# final_price = product_price - (discount_given * 100)
# print(final_price)



weight = float(input("enter the weight :"))
height = float(input("enter the height :"))
body_mass_index = weight / (height**2)
print(body_mass_index)
