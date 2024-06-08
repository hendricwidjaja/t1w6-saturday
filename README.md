# Python Term 1 Week 6 Saturday Class

# If-Else Practice Activity

## Building a Calculator
Build a calculator that takes 3 inputs from the user:
2 inputs as numbers(floats preferrably) for operation and 3rd input to decide which operation they want to perform

# Lists
Collection of values stored in a list
It is a composite data type, meaning multiple data types can be stored in one variable
Each piece is called an element

# Loops
Like Post Malone describes, "Run Away, but we're running in circles"
Used to repeat a block of code multiple times until a <strong>certain condition is met.</strong>

DRY coding principle: Don't Repeat Yourself

Example: Counting coins in your piggy bank

'If' condition would decide whether or not to run the indented block, whereas...
Loops will decide how many times the user wants to run the indented block

# While Loop
While the condition is met, keep executing the indented block. If not met, skip the block.

Things to consider:
    - Program can enter the loop
    - Program can exit the loop

## Range
Pre-defined function of Python (e.g. print) that generates a sequence of numbers.

Useful: Loops for iterating a specific number of times over a sequence of numbers.

range(1)
1 is a parameter
range(1, 2, 3)
1, 2 and 3 are all parameters
1 = starting number
2 = stopping number
3 = stepping number (go up the range by how many per step?)

## For Loop
For each item in a sequence, execute the indented statements.

for variable_name in sequence:
    statements...

## Practice Example 1
Finding the sum of the first ten numbers (1, 2, ... 10)

## Practice Example 2 
Find the largest number in the list
list = [3, 41, 12, 9, 74, 15]

# Loop Control Statements
Control the flow of the loop, terminate the loop early if you want or skip over some iterations

## Break statement
Terminate loop immediately and moves to the next statement after the loop.

## Continue statement
Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

# Nested Loops
A loop inside another loop! Inception.
Useful for running multi-dimensional structures, like MATRIX.

## Practice Example 1
Print a right-angled triangle pattern of stars.
*
**
***
****
*****

## Practice Example 2
Count the occurence of a letter in a list

# enumerate() function
Used to access the index and the value of the element of the list.
Use two variables in the for loop.
e.g. for index, animal in ....
The first variable stores the value of the index.
The second variable stores the value of the element

animals = ["cat", "dog", "rabbit", "horse"]

index would store = 0, 1, 2, 3
animal would store = cat, dog, rabbit, horse