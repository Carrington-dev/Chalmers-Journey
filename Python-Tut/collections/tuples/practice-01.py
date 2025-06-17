numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Accessing elements
first_number = numbers[0]  # First element
second_number = numbers[1]  # Second element
third_number = numbers[2]   # Third element
print("First number:", first_number)
print("Second number:", second_number)
print("Third number:", third_number)
names = ("Alice", "Bob", "Charlie", "David", "Eve")
first_name = names[0]       # First name    
second_name = names[1]      # Second name
third_name = names[2]       # Third name
print("First name:", first_name)
print("Second name:", second_name)
print("Third name:", third_name)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)   
print("Element at first row, second column:", matrix[0][1])  # Accessing the first element of the first row
print("Element at first row, third column:", matrix[0][2])  # Accessing the first element of the first row
# Accessing elements
first_row = matrix[0]      # First row
second_row = matrix[1]     # Second row
third_row = matrix[2]      # Third row
print("First row:", first_row)
print("Second row:", second_row)
print("Third row:", third_row)  
# Tuples are immutable, so we cannot append, pop, insert, or remove elements like we do with lists.
# However, we can create a new tuple with the desired changes.
# Adding a new number to the end of the tuple (creating a new tuple)
new_numbers = numbers + (11,)  # Adding 11 to the end of the tuple
print("Updated numbers:", new_numbers)
# Pop an element from the tuple (creating a new tuple)
popped_number = numbers[:-1]  # Removes the last element by slicing
print("Popped number:", popped_number)