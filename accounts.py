## Write a python program that reads in a 10 character account number
## and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# 1. create a function to get user to input account number:
# Reference:Reference: Andrew Beatty lectures week 2.

account_number = input("Please enter a 10-digit account number: ")

# 2. after account number is input,hide the first 6 digits with "xxxxxx"
# to access the first 6 digits use [6:]
# Reference Andrew Beatty lecture topic 5 data structures and associated jupyter notebook
# Reference: Chatgpt:prompt -how to hide first 6 digits of account number python,
#  https://chatgpt.com/c/680d6d03-cba4-8003-af4e-d11d931774e0

Hidden_account = "xxxxxx" + account_number[6:] 

# 3. then print the masked account number 

print(Hidden_account)

        