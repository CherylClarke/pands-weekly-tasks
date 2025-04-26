# pands-weekly-tasks
## weekly task 01
This file should contain a python program that displays Hello World! when it is run.

The Python program is the print() function, in which you type print followed by brackets that inclose the characters "Hello World!" which makes a string by adding the quotation marks each side. 

Should look like this : print("Hello World!")

For the code :
Reference: Andrew Beatty, week 01 example on pushing items from visual studio code to github repository

Also:
Reference: W3schools on python strings link: https://www.w3schools.com/python/python_strings.asp
Reference: Andrew beatty, week 03 Lecture on Strings




## weekly task 02
Write a program called bank.py 

The program should:

                Prompt the user and read in two money amounts (in cent)
                Add the two amounts
                Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180

The sum of these is €2.45
## weekly task 03
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890

Extra:

Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
## weekly task 04
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

Example of it running:

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1

## weekly task 05

Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.

An example of running this program on a Thursday is given below.

$ python weekday.py

Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py

It is the weekend, yay!
There is no user input.

## weekly task 06

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.