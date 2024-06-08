# Initialising a variable
string_list = ["Coder", "Academy", "Champion"]

result = 0
character_check = "a"


for word in string_list:
    for letter in word:
        if letter.lower() in character_check.lower():
            result += 1

print(f"Total occurence of {character_check} is: {result}")