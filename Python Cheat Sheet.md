# Python Quick Reference

This cheat sheet is a condensed reference for the Python concepts reviewed in Computer Science 25: variables and primitive types, input/output, conditions, and loops.    

---

## Variables and Primitive Data Types

Variables store values using the `=` assignment operator.

```python
name = "Alex"
age = 16
height = 1.72
likes_python = True
```

The basic data types you will use most often are:

| Type    | Stores            | Examples               |
| ------- | ----------------- | ---------------------- |
| `int`   | Whole numbers     | `5`, `-12`, `100`      |
| `float` | Decimal numbers   | `3.14`, `-0.5`, `10.0` |
| `str`   | Text              | `"Hello"`, `"Python"`  |
| `bool`  | True/false values | `True`, `False`        |

Use `type()` to check the type of a value.

```python
age = 16

print(type(age))
```

---

## Output

Use `print()` to display information.

```python
print("Hello!")
```

Variables can be printed directly.

```python
name = "Alex"

print(name)
```

### F-Strings

Use an **f-string** to insert values into text.

```python
name = "Alex"
score = 85

print(f"{name} earned {score} points.")
```

Place variables or expressions inside `{ }`.

```python
x = 5
y = 10

print(f"The total is {x + y}.")
```

---

## Input

Use `input()` to get information from the user.

```python
name = input("Enter your name: ")

print(f"Hello, {name}!")
```

`input()` always returns a `str`.

Convert input when you need another data type.

```python
age = int(input("Enter your age: "))
temperature = float(input("Enter the temperature: "))
```

A common pattern is:

```python
number = int(input("Enter a number: "))

result = number * 2

print(f"The result is {result}.")
```

---

# Conditions

## Comparison Operators

Comparison operators produce `True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

Example:

```python
age = 16

print(age >= 16)
```

---

## If Statements

Use `if` when code should only run when a condition is true.

```python
temperature = 30

if temperature > 25:
    print("It is hot outside.")
```

Remember:

* The condition ends with `:`.
* Code inside the condition must be indented.

---

## If / Else

Use `else` when something should happen if the condition is false.

```python
age = int(input("Enter your age: "))

if age >= 16:
    print("You can drive.")
else:
    print("You cannot drive yet.")
```

---

## If / Elif / Else

Use `elif` when there are several possible conditions.

```python
score = int(input("Enter your score: "))

if score >= 80:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 60:
    print("Satisfactory")
else:
    print("Keep practicing")
```

Python checks conditions from **top to bottom** and stops after it finds the first condition that is true.

---

## Combining Conditions

Use `and`, `or`, and `not` to combine or modify conditions.

### `and`

Both conditions must be true.

```python
age = 16
has_ticket = True

if age >= 14 and has_ticket:
    print("You may enter.")
```

### `or`

At least one condition must be true.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```

### `not`

Reverses a Boolean value.

```python
game_over = False

if not game_over:
    print("Keep playing.")
```

---

# For Loops

Use a `for` loop when you want to repeat something a known number of times or move through a sequence.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

---

## `range()`

### Stop

```python
for number in range(5):
    print(number)
```

Produces `0` through `4`.

### Start and Stop

```python
for number in range(1, 6):
    print(number)
```

Produces `1` through `5`.

### Start, Stop, and Step

```python
for number in range(0, 11, 2):
    print(number)
```

Produces:

```text
0
2
4
6
8
10
```

Remember:

```text
range(start, stop, step)
```

The `stop` value is **not included**.

---

## Using the Loop Variable

The loop variable changes each time through the loop.

```python
for number in range(1, 6):
    print(f"{number} squared is {number * number}")
```

---

## Traversing a String

A `for` loop can move through each character of a string.

```python
word = "Python"

for letter in word:
    print(letter)
```

This produces:

```text
P
y
t
h
o
n
```

You can combine traversal with conditions.

```python
word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count += 1

print(count)
```

---

# While Loops

Use a `while` loop when code should repeat **while a condition remains true**.

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

A `while` loop usually needs something inside it that eventually changes its condition.

Without this:

```python
number += 1
```

the example above would run forever.

---

## Repeating User Input

A common use for a `while` loop is repeating something until the user gives a particular answer.

```python
password = ""

while password != "python":
    password = input("Enter the password: ")

print("Access granted.")
```

---

## Input Validation

A `while` loop can force the user to provide a valid value.

```python
number = int(input("Enter a number from 1 to 10: "))

while number < 1 or number > 10:
    print("Invalid number.")
    number = int(input("Enter a number from 1 to 10: "))

print(f"You entered {number}.")
```

The general pattern is:

```python
value = input("Enter a value: ")

while value_is_invalid:
    value = input("Try again: ")
```

---

# Useful Operators

## Arithmetic

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `+`      | Addition         | `5 + 2`  |
| `-`      | Subtraction      | `5 - 2`  |
| `*`      | Multiplication   | `5 * 2`  |
| `/`      | Division         | `5 / 2`  |
| `//`     | Integer division | `5 // 2` |
| `%`      | Remainder        | `5 % 2`  |
| `**`     | Exponent         | `5 ** 2` |

### Checking Even or Odd

The `%` operator is useful for determining whether a number is even.

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Updating Variables

These statements do the same thing:

```python
score = score + 1
```

```python
score += 1
```

Other shorthand operators include:

```python
score -= 1
score *= 2
score /= 2
```

---

# Common Patterns

## Get a Number from the User

```python
number = int(input("Enter a number: "))
```

## Make a Decision

```python
if condition:
    # Code
elif another_condition:
    # Code
else:
    # Code
```

## Repeat a Specific Number of Times

```python
for i in range(10):
    # Code
```

## Repeat Through a Sequence

```python
for item in sequence:
    # Code
```

## Repeat Until Something Happens

```python
while condition:
    # Code
```

## Count Something

```python
count = 0

for item in sequence:
    if condition:
        count += 1
```

## Keep a Running Total

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

## Validate Input

```python
value = int(input("Enter a value: "))

while value < minimum or value > maximum:
    value = int(input("Invalid. Try again: "))
```

---

# Quick Syntax Reference

```python
# Variable
name = "Alex"

# Output
print("Hello")

# F-string
print(f"Hello, {name}!")

# Input
name = input("Name: ")

# Numeric input
age = int(input("Age: "))

# If
if age >= 16:
    print("Yes")

# If / else
if age >= 16:
    print("Yes")
else:
    print("No")

# If / elif / else
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")

# For loop
for i in range(10):
    print(i)

# Traverse a string
for letter in word:
    print(letter)

# While loop
while number < 10:
    number += 1
```
