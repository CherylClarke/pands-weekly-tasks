## 1st prompt the user and read in two money amounts in (cents)

# amount in cents are integer ,could check with- 
# print(type(65))
# Reference: https://www.w3schools.com/python/python_numbers.asp

# the names for the 2 money amounts will be (amount1) and (amount2)
# input a string to prompt user to input the cent amounts x 2 amounts, to ask the question.
# Reference: Andrew Beatty lectures week 2.
# Reference: Chatgpt, prompt was "in python, Prompt the user and read in two money amounts (in cent)"
# https://chatgpt.com/c/680d22bf-a100-8003-b9c8-65a593ae6a21

amount1 = int(input("enter amount 1 in cents: "))
amount2 = int(input("enter amount 2 in cents: "))


## add the 2 amounts
#  total is the 2 amounts added

total=(amount1 + amount2)

# to print the results:
#print to display,
#using the f sting to change the variable {total} to total when run 
# Andrew beatty lab 2.2 first programs
# Reference Chatgpt ,prompt was "add the 2 amounts, and print"
#  https://chatgpt.com/c/680d22bf-a100-8003-b9c8-65a593ae6a21 , 

print(f"The total amount is {total} cents.")



##print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
# need to finds the amounts in full euros(int) and second amount in cents the remander as a percentage
#floats cant be used as they are never accurate ,Reference Andrew Beatty

# to divide total by 100 use // ,to get euro amount, reference lectures in week 2. 
# to get percentage use % ,to get cent amount, reference lectures week 2.

euro= total // 100
cent= total % 100

# add in string to function you want printed, with euro and cent included
# add the 02d to make sure it only displays to 2 digits even if you have to add a 0

print(f"the sum of these is €{euro}.{cent:02d}")



