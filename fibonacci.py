#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


while True:
  user_input = input("Enter number of terms of the Fibonacci sequence: ")
  print("User input: ", user_input)

  
  if user_input.isdigit():
    num = int(user_input)
    if num > 0:
      break
    else:
      print("Please enter a positive integer.")
  else:
    print("Please enter a positive integer.")



print("Expected output: ")
    
a,b = 0, 1

if num >= 1:
  print(a, end=' ')

if num >= 2:
  print(b, end=' ')

if num > 3:
  for i in range(3, num + 1):
    total = a + b
    print(total, end=' ')
    a = b
    b = total
