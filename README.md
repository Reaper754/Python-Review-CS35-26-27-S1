# Python Programming Review — Computer Science 35

This activity is pass-fail. For each section you will be asked to create a Python file and perform a small review task. By completing each task, you will pass that task.

The tasks you should complete are as follows:

1. [Functions](#1-functions)
2. [Functions with Parameters](#2-functions-with-parameters)
3. [Functions that Return Values](#3-functions-that-return-values)
4. [Lists](#4-lists)
5. [Tuples](#5-tuples)
6. [Dictionaries](#6-dictionaries)
7. [2D Lists](#7-2d-lists)
8. [Linear Search](#8-linear-search)
9. [Bubble Sort](#9-bubble-sort)
10. [Merge Sort](#10-merge-sort)
11. [Final Review Challenge](#11-final-review-challenge)

By the end, you should have 11 distinct Python files that have been appropriately modified, and this assignment will be out of 11 marks.

This review assumes that you remember the introductory Python concepts from Computer Science 25, including variables, input/output, conditions, and loops. Refer to the Python Quick Reference if you need a reminder of these concepts.

---

# 1. Functions

A **function** is a named block of code that can be run whenever it is needed.

Functions are useful when a program needs to perform the same task multiple times.

A function is created using `def`.

```python
def print_welcome():
    print("--------------------")
    print("Welcome to the game!")
    print("--------------------")
```

Creating the function does not immediately run its code.

To run it, you **call** the function:

```python
def print_welcome():
    print("--------------------")
    print("Welcome to the game!")
    print("--------------------")


print_welcome()
```

A function can be called as many times as necessary.

```python
def print_welcome():
    print("--------------------")
    print("Welcome to the game!")
    print("--------------------")


print_welcome()
print_welcome()
print_welcome()
```

Functions help prevent duplicated code and make larger programs easier to organize.

## Try It

Create a new Python file named `functions.py`.

Copy and run this program:

```python
def print_separator():
    print("====================")


print_separator()
print("Python Review")
print_separator()
```

Modify `print_separator()` so that it prints a different separator.

Then call the function two additional times somewhere in your program.

## Create Your Own

In `functions.py`, create a function named:

```python
print_menu()
```

The function should display a menu similar to:

```text
1. Start Game
2. Instructions
3. Quit
```

Call `print_menu()` at least twice in your program.

---

# 2. Functions with Parameters

Functions become more useful when information can be passed into them.

A **parameter** is a variable that receives information when the function is called.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Alex")
greet("Sam")
```

The parameter `name` receives a different value each time the function is called.

Functions can accept multiple parameters.

```python
def print_score(name, score):
    print(f"{name} earned {score} points.")


print_score("Alex", 85)
print_score("Sam", 92)
```

The values supplied when calling a function are called **arguments**.

In:

```python
print_score("Alex", 85)
```

`"Alex"` and `85` are arguments.

## Try It

Create a new Python file named `function_parameters.py`.

Copy and run this program:

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Alex", 16)
introduce("Jordan", 17)
```

Modify the function so that it also accepts a favourite subject.

For example:

```text
My name is Alex, I am 16 years old, and my favourite subject is Computer Science.
```

## Create Your Own

In `function_parameters.py`, create a function named:

```python
calculate_area(width, height)
```

The function should calculate the area of a rectangle and print the result.

For example:

```python
calculate_area(5, 4)
```

should print:

```text
The area is 20.
```

Call your function at least three times using different arguments.

---

# 3. Functions that Return Values

Sometimes a function should calculate a value and send it back to the part of the program that called it.

This is done using `return`.

```python
def double(number):
    return number * 2


result = double(5)

print(result)
```

The function:

```python
double(5)
```

produces the value:

```text
10
```

That returned value can be stored in a variable.

```python
result = double(5)
```

It can also be used directly inside another expression.

```python
print(double(10))
```

## `print()` vs. `return`

These two functions behave differently:

```python
def add_and_print(a, b):
    print(a + b)
```

```python
def add_and_return(a, b):
    return a + b
```

The first function **displays** the answer.

The second function **gives the answer back to the program**, allowing the program to use it later.

For example:

```python
def add(a, b):
    return a + b


total = add(10, 5)
average = total / 2

print(average)
```

## Try It

Create a new Python file named `return_values.py`.

Copy and run this program:

```python
def square(number):
    return number * number


result = square(5)

print(result)
```

Modify the program so that it asks the user for a number and passes that number into `square()`.

## Create Your Own

In `return_values.py`, create a function named:

```python
larger_number(a, b)
```

The function should return whichever number is larger.

For example:

```python
result = larger_number(12, 7)

print(result)
```

should print:

```text
12
```

Test your function using at least three different pairs of numbers.

---

# 4. Lists

A **list** stores multiple values in a single variable.

```python
colours = ["red", "green", "blue"]
```

Each value has an **index**.

```text
Index:      0        1        2
Value:    "red"   "green"   "blue"
```

Python starts counting indexes at `0`.

You can access an individual value using its index.

```python
colours = ["red", "green", "blue"]

print(colours[0])
print(colours[2])
```

You can change an existing value:

```python
colours[1] = "yellow"
```

You can add a new value using `append()`:

```python
colours.append("purple")
```

You can remove a value using `remove()`:

```python
colours.remove("red")
```

Use `len()` to determine how many values are in a list.

```python
print(len(colours))
```

## Traversing a List

A `for` loop can visit every item in a list.

```python
colours = ["red", "green", "blue"]

for colour in colours:
    print(colour)
```

You can also traverse using indexes.

```python
for i in range(len(colours)):
    print(colours[i])
```

The second version is particularly useful when you need the location of an item rather than only its value.

## Try It

Create a new Python file named `lists.py`.

Copy and run this program:

```python
games = ["Minecraft", "Portal", "Tetris"]

games.append("Celeste")

for game in games:
    print(game)
```

Modify the program so that:

1. You add another game.
2. You change one existing game.
3. You print the total number of games.

## Create Your Own

In `lists.py`, create a list containing five numbers.

Use a loop to calculate the total of all numbers in the list.

Do not manually add the five indexes together.

For example:

```python
numbers = [5, 8, 2, 10, 4]
```

should eventually produce:

```text
Total: 29
```

---

# 5. Tuples

A **tuple** is similar to a list, but its values cannot normally be changed after the tuple is created.

Lists use square brackets:

```python
coordinates = [10, 20]
```

Tuples use parentheses:

```python
coordinates = (10, 20)
```

Values are accessed using indexes just like a list.

```python
coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])
```

Tuples are useful for groups of values that belong together and should not change.

For example:

```python
player_position = (250, 120)
rgb_colour = (255, 100, 50)
screen_size = (1920, 1080)
```

You can traverse a tuple with a `for` loop.

```python
rgb_colour = (255, 100, 50)

for value in rgb_colour:
    print(value)
```

## Try It

Create a new Python file named `tuples.py`.

Create this tuple:

```python
screen_size = (1920, 1080)
```

Print the width and height separately.

Your output should look similar to:

```text
Width: 1920
Height: 1080
```

## Create Your Own

In `tuples.py`, create a tuple representing an RGB colour.

For example:

```python
colour = (120, 200, 75)
```

Use indexes to print:

```text
Red: 120
Green: 200
Blue: 75
```

Then use a `for` loop to print all three values.

---

# 6. Dictionaries

A **dictionary** stores information as **key-value pairs**.

```python
student = {
    "name": "Alex",
    "age": 16,
    "grade": 11
}
```

Instead of accessing information using a numerical index, you use a key.

```python
print(student["name"])
print(student["age"])
```

You can change a value:

```python
student["age"] = 17
```

You can add a new key-value pair:

```python
student["favourite_subject"] = "Computer Science"
```

## Traversing a Dictionary

You can loop through the keys:

```python
student = {
    "name": "Alex",
    "age": 16,
    "grade": 11
}

for key in student:
    print(key)
```

You can use the key to access each value:

```python
for key in student:
    print(f"{key}: {student[key]}")
```

You can also use `.items()` to access both at once.

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

## Try It

Create a new Python file named `dictionaries.py`.

Copy and run this program:

```python
game = {
    "title": "Tetris",
    "year": 1985,
    "players": 1
}

for key, value in game.items():
    print(f"{key}: {value}")
```

Add two additional pieces of information to the dictionary.

## Create Your Own

In `dictionaries.py`, create a dictionary describing a fictional character.

Include at least:

* Name
* Health
* Level
* Character class

Print each piece of information using a loop.

Then change the character's health and print the updated dictionary.

---

# 7. 2D Lists

A **2D list** is a list containing other lists.

It is useful for representing information arranged into rows and columns.

For example:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

The first index chooses the **row**.

The second index chooses the **column**.

```python
print(grid[0][0])
```

prints:

```text
1
```

While:

```python
print(grid[1][2])
```

prints:

```text
6
```

Think of:

```python
grid[row][column]
```

## Traversing a 2D List

Because a 2D list contains lists inside another list, you normally use **nested loops**.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for value in row:
        print(value)
```

You can also traverse using indexes.

```python
for row in range(len(grid)):
    for column in range(len(grid[row])):
        print(grid[row][column])
```

Using indexes is particularly useful when you need to know the position of a value.

```python
for row in range(len(grid)):
    for column in range(len(grid[row])):
        print(f"Row {row}, Column {column}: {grid[row][column]}")
```

## Try It

Create a new Python file named `two_dimensional_lists.py`.

Create this grid:

```python
grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]
```

Use nested loops to print every value.

Then print only the value located at row `1`, column `2`.

## Create Your Own

Replace the grid with:

```python
numbers = [
    [5, 8, 2],
    [10, 3, 7],
    [4, 9, 6]
]
```

Use nested loops to calculate the total of **every number** in the 2D list.

Your program should produce:

```text
Total: 54
```

---

# 8. Linear Search

A **search algorithm** looks through a collection of data to find a particular value.

A **linear search** starts at the beginning and checks values one at a time until the target is found.

Consider:

```python
numbers = [12, 7, 25, 4, 18]
```

To find `25`, a linear search checks:

```text
12 → not 25
7  → not 25
25 → found
```

A basic linear search function looks like this:

```python
def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i

    return -1
```

The function returns the index where the value was found.

If the value does not exist, it returns `-1`.

```python
numbers = [12, 7, 25, 4, 18]

index = linear_search(numbers, 25)

print(index)
```

Output:

```text
2
```

## Try It

Create a new Python file named `linear_search.py`.

Copy and run this program:

```python
def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i

    return -1


names = ["Alex", "Jordan", "Sam", "Taylor", "Morgan"]

result = linear_search(names, "Sam")

print(result)
```

Run the search several times using different names.

Try searching for a name that does not exist.

## Create Your Own

Modify `linear_search.py` so that the user enters the name they want to find. Then, each iteration of the search print a message that indicates which iteration of the search the loop is on, and the name at that index.

For example:

```text
Enter a name: Taylor

At index 0 is Alex.
At index 1 is Jordan.
At index 2 is Sam.
At index 3 is Taylor.
Taylor found at index 3.
```

If the name is not found:

```text
Enter a name: Chris

At index 0 is Alex.
At index 1 is Jordan.
At index 2 is Sam.
At index 3 is Taylor.
At index 4 is Morgan.
Chris was not found.
```

---

# 9. Bubble Sort

A **sorting algorithm** rearranges data into a particular order.

Bubble sort repeatedly compares values that are beside each other.

If the values are in the wrong order, they are swapped.

Consider:

```text
5  2  8  1
```

Bubble sort starts by comparing:

```text
5 and 2
```

Because `5 > 2`, they are swapped:

```text
2  5  8  1
```

It then compares `5` and `8`.

No swap is needed.

Then it compares `8` and `1`:

```text
2  5  1  8
```

After one complete pass, the largest unsorted value has moved toward the end.

Bubble sort repeats these passes until the list is sorted.

A basic implementation is:

```python
def bubble_sort(values):
    for pass_number in range(len(values) - 1):
        for i in range(len(values) - 1 - pass_number):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
```

The swap:

```python
temp = values[i]
values[i] = values[i + 1]
values[i + 1] = temp
```

could also be written in Python as:

```python
values[i], values[i + 1] = values[i + 1], values[i]
```

For this review, make sure you understand **why the swap happens** rather than simply memorizing the shorter Python syntax.

## Try It

Create a new Python file named `bubble_sort.py`.

Copy and run this program:

```python
def bubble_sort(values):
    for pass_number in range(len(values) - 1):
        for i in range(len(values) - 1 - pass_number):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp


numbers = [8, 3, 6, 1, 7, 2]

print(numbers)

bubble_sort(numbers)

print(numbers)
```

Change the numbers in the original list and test the algorithm again.

## Create Your Own

Modify `bubble_sort.py` so that the program prints the list after **every pass** through the outer loop.

For example, you should be able to see the list gradually becoming sorted.

You will need to decide where this statement belongs:

```python
print(values)
```

---

# 10. Merge Sort

Merge sort sorts data by breaking a large problem into smaller problems and then combining the sorted results.

For example:

```text
[8, 3, 6, 2]
```

can be divided into:

```text
[8, 3]    [6, 2]
```

and then:

```text
[8] [3]   [6] [2]
```

Single-item lists are already sorted.

The values can then be merged back together in order:

```text
[3, 8]    [2, 6]
```

and finally:

```text
[2, 3, 6, 8]
```

The important part of merge sort is the **merge operation**.

Two already-sorted lists can be combined by repeatedly comparing the value at the front of each list.

```python
def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result
```

For example:

```python
left = [2, 5, 8]
right = [1, 4, 7]

print(merge(left, right))
```

produces:

```text
[1, 2, 4, 5, 7, 8]
```

A complete merge sort repeatedly divides the list and uses the merge operation to put it back together in sorted order.

```python
def merge_sort(values):
    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)
```

Combined:

```python
def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort(values):
    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)


numbers = [8, 3, 6, 1, 7, 2]

numbers = merge_sort(numbers)

print(numbers)
```

## Try It

Create a new Python file named `merge_sort.py`.

Copy and run the complete merge sort program above.

Change the list to:

```python
numbers = [12, 4, 9, 2, 15, 7, 1, 10]
```

Before running the program, predict what the final sorted list will contain.

Then run it and check your prediction.

## Create Your Own

Add temporary output statements to the `merge()` function so that you can see which lists are being merged.

For example:

```python
print(f"Merging {left} and {right}")
```

Run the algorithm again and watch how increasingly larger sorted lists are built.

Once you understand the process, remove the temporary output.

---

# 11. Final Review Challenge

Create a new Python file named `score_analyzer.py`.

Create a program called **Score Analyzer**.

Start with this list:

```python
scores = [72, 91, 64, 85, 78, 95, 68, 88]
```

Your program must contain the following functions:

```python
def calculate_average(scores):
```

This function should:

* Accept the list of scores.
* Calculate their average.
* Return the average.

---

```python
def linear_search(values, target):
```

This function should:

* Search the list for a particular score.
* Return its index if it is found.
* Return `-1` if it is not found.

---

```python
def bubble_sort(values):
```

This function should:

* Sort the scores from lowest to highest.

---

Your main program should:

1. Print the original list.
2. Calculate and print the average.
3. Ask the user for a score to search for.
4. Use your linear search function to find the score.
5. Tell the user whether the score was found.
6. Sort the scores.
7. Print the sorted list.

Example:

```text
Scores: [72, 91, 64, 85, 78, 95, 68, 88]

Average: 80.125

Enter a score to search for: 85
85 was found at index 3.

Sorted Scores: [64, 68, 72, 78, 85, 88, 91, 95]
```

Your program should demonstrate that you can use:

* Functions
* Parameters
* Return values
* Lists
* Loops
* Conditions
* Linear search
* Bubble sort

---

# Review Checklist

Before moving on, make sure you can do each of the following without copying an example.

* [ ] Define and call a function.
* [ ] Explain why functions are useful.
* [ ] Create a function that accepts parameters.
* [ ] Pass arguments into a function.
* [ ] Create a function that returns a value.
* [ ] Explain the difference between `print()` and `return`.
* [ ] Create and modify a list.
* [ ] Access a list item using an index.
* [ ] Add values to a list.
* [ ] Traverse a list using a loop.
* [ ] Create and access a tuple.
* [ ] Explain an important difference between a list and a tuple.
* [ ] Create a dictionary.
* [ ] Access dictionary values using keys.
* [ ] Add and modify dictionary values.
* [ ] Traverse a dictionary.
* [ ] Create a 2D list.
* [ ] Access a value using `list[row][column]`.
* [ ] Traverse a 2D list using nested loops.
* [ ] Explain how a linear search works.
* [ ] Implement a linear search.
* [ ] Explain how bubble sort works.
* [ ] Implement a bubble sort.
* [ ] Explain the purpose of swapping values during bubble sort.
* [ ] Explain how merge sort divides and combines data.
* [ ] Trace the merging of two sorted lists.
* [ ] Use functions and data structures together in a larger program.

---

# Using AI for Extra Review

If there is a topic from this review that you do not remember well, you can use an AI assistant to give you additional practice.

The goal is **not** to have the AI write programs for you. Instead, use it as a tutor that gives you small programming challenges, checks your attempts, and helps you understand mistakes.

Possible topics include:

* Functions
* Parameters and arguments
* Return values
* Lists
* Tuples
* Dictionaries
* 2D lists
* Nested loops
* Linear search
* Bubble sort
* Merge sort

## AI Practice Prompt

For additional practice with a topic, copy and paste this prompt into an LLM of your choice, replacing `[TOPIC]` with the topic you would like more practice with.

```text
I am reviewing Python programming and need more practice with [TOPIC].

Act as a programming tutor. Give me one small Python programming challenge at a time that focuses specifically on [TOPIC].

Do not give me the solution before I attempt the problem.

For each challenge:

1. Briefly explain any important concept I need to remember.
2. Give me a small programming task to complete.
3. Wait for me to write my code.
4. Check my code and tell me whether it works.
5. If I make a mistake, explain what is wrong without immediately giving me the completed solution.
6. Give me a hint and allow me to try again.
7. Once I solve the problem, briefly explain why my solution works.
8. Give me another challenge that is slightly more difficult.

Keep the programs short and appropriate for someone reviewing intermediate Python.

Continue until I tell you to stop.
```
