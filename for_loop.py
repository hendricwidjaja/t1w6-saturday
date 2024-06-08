# Range arguments (start, stop, step)

# print(range(5, 10, 1))

# For Loop in a range (as 'step' is not defined, default step is 1. Stop is defined as 10, so stops at "9")
for each in range(1, 10):
    print(each)

# If start and step is not defined, range will start from 0 and end 1 before the stop definition
for each in range(5):
    print(each)

# For Loop in a list
fruits = ["Apple", "Banana", "Cherry"]

for each in fruits:
    print(each)

for each in "CoderAcademy":
    print(each)

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")