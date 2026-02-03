#The else keyword catches anything which isn't caught by the preceding conditions.
#The else statement is executed when the if condition (and any elif conditions) evaluate to False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#The else statement must come last. You cannot have an elif after an else.
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Checking even or odd numbers:
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Validating user input:
username = "Emil"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")