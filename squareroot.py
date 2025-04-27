# You should create a function called <tt>sqrt</tt> that does this.
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root

# get user to input postive float point number

while True:
    try:
        number = float(input("Enter a number to be squared : "))
        if number > 0:
            print(f"You entered: {number}")
            break
        else:
            print("Please enter a number greater than zero.")
    except ValueError:
        



