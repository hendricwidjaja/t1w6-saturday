numbers = [3, 41, 12, 9, 74, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is", largest)