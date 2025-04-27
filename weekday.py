# Write a program that outputs whether or not today is a weekday. 

#Reference: geeksforgeeks.com- https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/


#import date and time function
import datetime

# Get today's date ,by using function below

today = datetime.datetime.today().weekday()

# Reference : chatgpt.com - prompt , what does weekday() do? https://chatgpt.com/c/680d7a1a-4d54-8003-8840-3fdd7ffaca05

# weekday() returns 0 (Monday) to 6 (Sunday)
# each day is represented by an integer 0-4 for monday to friday and 5-6 for saturday and sunday

# ask "if" today is less that 5, if yes print this "Yes, unfortunately today is a weekday" for weekday 
# or else if not less than 5 print this "No, today is a weekend! Enjoy!" for weekend
if today < 5:

    print("Yes, unfortunately today is a weekday.")
    
else:
    print("Its the weekend, Yay!")


