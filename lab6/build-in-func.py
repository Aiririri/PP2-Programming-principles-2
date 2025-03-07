from functools import reduce
import time
import math

# Write a Python program with builtin function to multiply all the numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
print(multiply_list(numbers))  # Output: 120

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"Uppercase letters": upper, "Lowercase letter": lower}

txt = "SererASDafDdfSDG"
print(count_case(txt)) # {'Uppercase letters': 8, 'Lowercase letter': 8}

# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(s):
    return s == s[::-1]

word = "diid"
print(is_palindrome(word)) # True

# Write a Python program that invoke square root function after specific milliseconds.

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")


num = int(input("Enter number: "))  
delay = int(input("Enter delay in milliseconds: "))  

delayed_sqrt(num, delay)

# Write a Python program with builtin function that returns True if all elements of the tuple are true.

def all_true(t):
    return all(t)


tup1 = (True, True, True)
tup2 = (True, False, True)

print(all_true(tup1))  # Output: True
print(all_true(tup2))  # Output: False

