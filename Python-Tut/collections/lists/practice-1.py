numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Accessing elements
first_number = numbers[0]  # First element
second_number = numbers[1]  # Second element
third_number = numbers[2]   # Third element


print("First number:", first_number)
print("Second number:", second_number)
print("Third number:", third_number)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
first_name = names[0]       # First name
second_name = names[1]      # Second name
third_name = names[2]       # Third name
print(names[0])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # Accessing the first element of the first row
print(matrix[0][2])  # Accessing the first element of the first row
# Accessing elements
first_row = matrix[0]      # First row
second_row = matrix[1]     # Second row
third_row = matrix[2]      # Third row

numbers.append(11)  # Adding a new number to the end of the list
print("Updated numbers:", numbers)
# Pop an element from the list
popped_number = numbers.pop()  # Removes the last element
print("Popped number:", popped_number)

# Insert an element at a specific position
numbers.insert(0, 20)  # Insert 20 at the beginning of the list
print("Numbers after insertion:", numbers)
# Remove an element by value
numbers.remove(5)  # Removes the first occurrence of 5
print("Numbers after removal:", numbers)