#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.j
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
While true:
 user_input = input("Enter the number of terms: ")
if user_input.isdigit():
  n = int(user_input)
  if n > 0:
    break
