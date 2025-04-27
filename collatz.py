# Write a program, that asks the user to input any positive integer
#  and outputs the successive values of the following calculation.

# At each step calculate the next value by taking the current value and,
#  if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.


def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)

# to see if the value input would have a remainder that would be the same as 0, when divided by 2
# the condition would be fulfilled and print results
#Reference: 365datascience.com https://365datascience.com/question/please-explain-if-x-2-0/ 
    else:
        result = 3 * number + 1
        print(result)
    return result
# else muiltple result by 3 and add 1
try:
    n = int(input("Enter a positive integer: "))
    while n != 1:
        n = collatz(n)
# to make sure input is an integer (n), keep loop going until n = 1
# Reference Chat gpt : prompt -explain collatz.py, https://chatgpt.com/c/680d7a1a-4d54-8003-8840-3fdd7ffaca05
except ValueError:
    print("Please enter a valid integer.")
# this is to print error if integer is not input by user