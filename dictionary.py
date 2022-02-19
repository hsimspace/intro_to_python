
# Creating a dictionary
# Values and keys can't be duplicated 
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Creating another dictionary with keys of type number
month_conversions_1 = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

# Accessing dictionary elements
print(month_conversions["Jan"])

# Another way to access dictionary elements
print(month_conversions.get("Dec"))

# Searching non-mappable element
print(month_conversions.get("Luv"))
print(month_conversions.get("Luv", "Not a valid key"))

# Accessing elements of the new dictionary
print(month_conversions_1[0])














