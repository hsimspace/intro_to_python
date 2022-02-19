# Create two dimensional list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Access the first number in the first row
print(number_grid[0][0])

# Accessing the second number in the third row
print(number_grid[2][1])

# Use for loops to access all the numbers in this list
for row in range(len(number_grid)):
    for col in range(len(number_grid[row])):
        print(number_grid[row][col])




















