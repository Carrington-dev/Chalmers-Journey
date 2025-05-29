# Chalmers-Journey
Chalmers Software Engineering Tutorial
Great! Here's an extended **Python Structure** guide including **Loops**, **Functions**, **Lists**, and **Error Handling** — in addition to **Variables**, **Input**, and **Conditions**:

---

## **PYTHON STRUCTURE**

---

### **a. Variables**

Used to store data.

```python
name = "Alice"      # String
age = 30            # Integer
height = 1.75       # Float
is_happy = True     # Boolean
```

---

### **b. Input**

Takes input from the user (returns string by default).

```python
username = input("Enter your name: ")
age = int(input("Enter your age: "))
```

---

### **c. Conditions**

Controls flow based on conditions.

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

---

### **d. Loops**

#### **For Loop**

Used to iterate over a sequence (like list, range, etc.).

```python
for i in range(5):
    print("Number:", i)
```

#### **While Loop**

Repeats as long as a condition is `True`.

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

---

### **e. Functions**

Reusable blocks of code.

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
```

**With return value:**

```python
def add(x, y):
    return x + y

result = add(5, 3)
print("Sum:", result)
```

---

### **f. Lists**

Used to store multiple items.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # Access
fruits.append("pear")   # Add
fruits.remove("banana") # Remove
```

---

### **g. Error Handling**

Catch and handle errors using `try-except`.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done.")
```

---

Would you like me to turn this into a PDF, printable guide, or interactive notebook?
