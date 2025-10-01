#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


while True:
  user_input = int(input("Enter number of terms of the Fibonacci sequence: "))
  
  if num > 0:
    break
  else:
    print("Please enter a positive integer.")


a,b = 0, 1

for i in range(n):
  if i == 0:
    print(a, end='')
  elif i == 1:
    print(b, end='')
  else:
    c = a + b
    print (c, end='')
    a,b = b,c
