# pands-weekly-tasks
## weekly task 01
This file should contain a python program that displays Hello World! when it is run.
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