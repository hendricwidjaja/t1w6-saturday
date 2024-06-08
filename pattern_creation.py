# Create a right-angled triangle of stars ( * ) with max length of 5 *

stars = 5

for i in range(1, stars + 1, 1):
    for j in range(i):
        print("*", end="")
    print()