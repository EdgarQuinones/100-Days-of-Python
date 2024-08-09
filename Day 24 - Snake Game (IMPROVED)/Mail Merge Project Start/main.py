# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Gets list of names
with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

# Gets rid of new line character
for index in range(len(names)):
    names[index] = names[index].strip()

# Get a copy of the letter template
with open("Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

# Make specified letters
for name in names:
    letter_name = f"letter_for_{name}"
    new_letter = letter.replace("[name]", name)
    with open(f"ReadyToSend/{letter_name}", mode="w") as file:
        file.write(new_letter)
