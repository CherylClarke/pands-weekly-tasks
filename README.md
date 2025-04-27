# pands-weekly-tasks
## weekly task 01
## helloworld.py
This file should contain a python program that displays Hello World! when it is run.

The Python program is the print() function, in which you type print followed by brackets that inclose the characters "Hello World!" which makes a string by adding the quotation marks each side. 

Should look like this : print("Hello World!")

For the code :
Reference: Andrew Beatty, week 01 example on pushing items from visual studio code to github repository

Also:
Reference: W3schools on python strings link: https://www.w3schools.com/python/python_strings.asp

Reference: Andrew beatty, week 03 Lecture on Strings




## weekly task 02
## bank.py

Write a program called bank.py 

The program should:

1. Prompt the user and read in two money amounts (in cent)
First must prompt the user to input 2 different money amounts in cents.
Name the money amounts will be (amount1) and (amount2)

both amounts are already integers but if you wanted to check this you could check with
"print(type(65))"for amount1 for example
Reference: W3shools (2025). Python numbers. [online] Available at : https://www.w3schools.com/python/python_numbers.asp [Accessed 26 April 2025]

Input string to prompt user to input cent amount, (this will ask the question)
do this for both amount1 and then amount2

Reference: Andrew beatty lectures week 2.
Reference: Chatgpt,prompt- in python, prompt the user and read in two money amounts (in cent)
https://chatgpt.com/c/680d22bf-a100-8003-b9c8-65a593ae6a21,[Accesssed 26 April 2025].

amount1 = int(input("enter amount 1 in cents: "))

int for integer amount, input for the string you want printed(the question), and : for the answer to be input by user
do for both

2. Add the two amounts

I am going to use "total" for the sum of both amount1 and amount2.

eg. total=(amount1 + amount2)

then to display the results use print function
will using the f sting to change the variable {total} to total when run

eg. print(f"The total amount is {total} cents.")

Reference: Andrew beatty lab 2.2 first programs
Reference: Chatgpt, prompt was "add the 2 amounts, and print"
https://chatgpt.com/c/680d22bf-a100-8003-b9c8-65a593ae6a21 [Accessed 26 April 2025]. 


3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

First I need to finds the amount in full euros(int) and second amount in cents the remander as a percentage.

first divide total by 100 use // ,to get euro amount


Going to make "euro" = the result
eg. euro= total // 100

Reference: lectures in week 2.

Reference: stackoverflow. (2025). / v // for division in Python. [online] Available at:  https://stackoverflow.com/questions/183853/vs-for-division-in-python/183870#183870` [Accessed 26 April 2025]

Reference: Quickref.Me.(2025) Python cheatsheet(online) Available at:https://quickref.me/python.html [Accessed 20 April. 2025]


Secondly to get percentage use % ,to get cent amount.

Im going to make "cent" = the result
cent= total % 100


Reference:Andrew Beatty lectures week 2.
Reference:  Quickref.Me.(2025) Python cheatsheet(online) Available at:https://quickref.me/python.html [Accessed 20 April. 2025]

add in string to function you want printed, with euro and cent included
add the 02d to make sure it only displays to 2 digits even if you have to add a 0

print(f"the sum of these is €{euro}.{cent:02d}")













## weekly task 03
## account.py
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).


1. create a function to get user to input a 10 digit account number
Reference:Reference: Andrew Beatty lectures week 2.

account_number = input("Please enter a 10-digit account number: ")

2. after account number is input,hide the first 6 digits with "xxxxxx"
to access the first 6 digits use [6:] and replace them with "xxxxxx"

Reference Andrew Beatty lecture topic 5 data structures and associated jupyter notebook
Reference: Chatgpt:prompt -how to hide first 6 digits of account number python,
 https://chatgpt.com/c/680d6d03-cba4-8003-af4e-d11d931774e0. [Accessed 26 April 2025]

Hidden_account = "xxxxxx" + account_number[6:] 

3. then print the hidden account number 

print(Hidden_account)

        
## weekly task 04
## collatz.py

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

input an integer
At each step calculate the next value by taking the current value and,

-if it is even, divide it by two, 
else
-if it is odd, multiply it by three and add one.


def collatz(number):
if number % 2 == 0:
result = number // 2
print(result)

to see if the value input would have a remainder that would be the same as 0, when divided by 2

the condition would be fulfilled and print results

Reference: 365datascience.com(2023). explaining if x % 2 == 0. [online] Available at: https://365datascience.com/question/please-explain-if-x-2-0/  [accessed 26 April 2025] 

else:
result = 3 * number + 1
print(result)
return result

else muiltple result by 3 and add 1




and try:
n = int(input("Enter a positive integer: "))
while n != 1:
n = collatz(n)

-to make sure input is an integer (n), keep loop going until n = 1

Reference: Chat gpt - prompt -explain collatz.py, https://chatgpt.com/c/680d7a1a-4d54-8003-8840-3fdd7ffaca05[Accessed 26 April 2025]

except ValueError:
    print("Please enter a valid integer.")

-this is to print error if integer is not input by user






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