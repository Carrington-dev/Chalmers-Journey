numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Print the first and last elements of the list.
print("First element:", numbers[0]) 
print(numbers[1: 5])  # Last element using negative indexing
print("Last element:", numbers[-1])
# 2. Print the first three elements of the list.
print("First three elements:", numbers[:3])  # Slicing to get the first three elements

for i in range(1, 9, 2):
    print(numbers[i], end=" ")  # Print odd numbers from 1 to 10
    # print(numbers[i+1], end=" ")  # Print odd numbers from 1 to 10