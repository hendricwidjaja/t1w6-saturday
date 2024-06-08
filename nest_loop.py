# A list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# prints
# print(matrix[1][1])

# for row in matrix:
#     for item in row:
#         print(item, end= " ")
#     print()

for row in matrix:
    for item in row:
        if item == row[1]:
            print(item, end=" ")
    print()
