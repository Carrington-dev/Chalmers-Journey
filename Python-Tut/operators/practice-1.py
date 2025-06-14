a = False
b = True
c = False
d = False

# Logical AND
result_and = a and b
# Logical OR
result_or = a or b
# Logical NOT
result_not_a = not a
result_not_b = not b

print("Logical AND (a and b):", result_and)
print("Logical OR (a or b):", result_or)
print("Logical NOT (not a):", result_not_a)
print("Logical NOT (not b):", result_not_b)
print("_____________________________________________________")
# Example of using logical operators in a conditional statement
if a and b:
    print("Both a and b are True.")
if c or d:
    print("Either c or d is True.")
if not a:
    print("a is False.")
print("_____________________________________________________")
print(a and b)
print(a or b)
print((not a) and b)
print((not a) or b)
print((not a) or (not b))