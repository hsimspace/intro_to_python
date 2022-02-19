
# Getting input from the user
# Using try -- except block
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")
'''
# You can specify the type of error you are
# wanting to catch
# We can store the error as a variable which 
# can be manipulated
try:
    value = 10/0    # This will also get caught by the exception
    # as an invalid input unless we make it specific
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")















