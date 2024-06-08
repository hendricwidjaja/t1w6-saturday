# i = 0
# break loop (prints = 0, 1 and 2 consecutively)
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# continue loop (prints = 1, 2, 4, 5)
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# Skipping vowels from a text
text = "Coder Academy"
vowels = "aeiouAEIOU"

for each in text:
    if each in vowels:
        continue
    print(each, end=" ")

print()

# Stop when there is "stop"
signals = ["start", "halt", "continue", "start", "stop", "hold", "halt", "go"]

for each_item in signals:
    if each_item == "stop":
        break
    print(each)