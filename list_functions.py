# Create different lists 
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# print
print(friends)

# Adding an element to the end of the list
friends.append("Creed")

# You can also add the element at a specific position
friends.insert(1, "Kelly")
print(friends)

# Removing elements
friends.remove("Jim")


# Append another list to an list
friends.extend(lucky_numbers)
print(friends)

# Removing all elements from the list
friends.clear()
print(friends)

# Reusing the list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(2, "Jim")
print(friends)

# Removing the final element
friends.pop()
print(friends)

# Identify the indices
# If you try to find the index of a foreing element
# It will give an error message
print("The index for oscar is:", friends.index("Oscar"))

# You can count how many times an element
# is repeated in the list
print("Jim is found", friends.count("Jim"), "times")

# Sorting number lists in ascending order
lucky_numbers.sort()
print(lucky_numbers)

# Sorting string lists in ascending order
friends.sort()
print(friends)

# You can reverse a list
# This is not sorting in descending order
lucky_numbers.reverse()
print(lucky_numbers)

# To sort in reverse order
# list.sort(reverse=True)
# sorted(list, reverse=True)

# *** Remember that a list can contain any form of data sturcture
# random list
# take second element for sort
# This is a bit more advanced, but flow with me
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)


# A list of dictionaries
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')































