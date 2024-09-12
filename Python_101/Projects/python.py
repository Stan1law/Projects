# A program that will display the age entered by the user

age = int(input("Enter age: "))
print("You are", age, " years old")


# A program that will accept the first name, middle initial, and last name of the user and
# then display the user's full name.

first_name = input("Enter first name: ")
middle_initial = input("Enter middle initial: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + middle_initial + ". " + last_name

print("Your full name is:", full_name)


# A program that will compute and display the average of 3 numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("The average of", num1, ",", num2, "and", num3, "is", float(average))


