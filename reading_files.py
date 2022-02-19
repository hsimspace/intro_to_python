# Reading external files into python
# open("employees.txt", "w") # write mode
# open("employees.txt", "r+") # read and write
# open("employees.txt", "a") # append mode
# employee_file.close() # when you finish

employee_file = open("employees.txt", "r") # read mode

print(employee_file.readable()) # Returns T or False

# Reading the entire file
#print(employee_file.read())

# Read just one line
#print(employee_file.readline()) # readline() moves the cursor to the
                                # next line after reading the previous one
#cleprint(employee_file.readline())

# We can put every line in a list
# print(employee_file.readlines()) # which is not readline()

# Use for loop to readlines
for employee in employee_file.readlines():
    print(employee)
























