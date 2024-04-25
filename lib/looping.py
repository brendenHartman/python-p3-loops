#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [int * int for int in int_list]

def fizzbuzz():
    i = 1
    while i < 101:
        i_3 = i % 3 == 0
        i_5 = i % 5 == 0
        if i_3 and i_5:
            print("FizzBuzz")
        elif i_3:
            print("Fizz")
        elif i_5: 
            print("Buzz")
        else:
            print(i)
        i += 1
