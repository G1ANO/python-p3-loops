#!/usr/bin/env python3

def happy_new_year():
    # Use a while loop to count down from 10 to 1
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # Use a list comprehension to square each integer
    return [num ** 2 for num in int_list]

def fizzbuzz():
    # Use a for loop to iterate from 1 to 100
    for num in range(1, 101):
        if num % 15 == 0:  # Divisible by both 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Divisible by 3
            print("Fizz")
        elif num % 5 == 0:  # Divisible by 5
            print("Buzz")
        else:
            print(num)
